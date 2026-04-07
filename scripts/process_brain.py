#!/usr/bin/env python3
"""
Process the beedee second brain: generate embeddings for notes and entities,
compute cross-connections via cosine similarity, cluster, and output a unified
graph structure for D3 visualization.
"""

import json
from pathlib import Path
from datetime import datetime
from collections import Counter

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

try:
    import hdbscan
    HDBSCAN_AVAILABLE = True
except ImportError:
    HDBSCAN_AVAILABLE = False

# Configuration
MIN_NODES_FOR_CLUSTERING = 10
MIN_CLUSTER_SIZE = 3
SIMILARITY_THRESHOLD = 0.5
MAX_CONNECTIONS_PER_NODE = 5
MODEL_NAME = "all-MiniLM-L6-v2"

# Paths
REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "data"
NOTES_RAW = DATA_DIR / "notes_raw.json"
COMPANIES = DATA_DIR / "companies.json"
FRAMEWORKS = DATA_DIR / "frameworks.json"
TOPICS = DATA_DIR / "topics.json"
OUTPUT = DATA_DIR / "brain_processed.json"


def load_json(path: Path):
    if path.exists():
        return json.loads(path.read_text())
    return {}


def save_json(path: Path, data: dict):
    path.write_text(json.dumps(data, indent=2))


def build_node_list():
    """Load all data sources and build a unified list of nodes with text for embedding."""
    nodes = []

    # Notes (append-only events)
    raw = load_json(NOTES_RAW)
    for note in raw.get("notes", []):
        text_for_embedding = f"{note.get('subject', '')}. {note.get('text', '')}"
        nodes.append({
            "id": note["id"],
            "type": "note",
            "text": note.get("text", ""),
            "subject": note.get("subject"),
            "timestamp": note.get("timestamp"),
            "source": note.get("source", "unknown"),
            "_embed_text": text_for_embedding,
        })

    # Companies (mutable entities)
    companies = load_json(COMPANIES)
    for slug, co in companies.items():
        parts = [co.get("name", ""), co.get("description", ""), co.get("my_understanding", "")]
        text_for_embedding = ". ".join(p for p in parts if p)
        nodes.append({
            "id": slug,
            "type": "company",
            "name": co.get("name", slug),
            "description": co.get("description", ""),
            "my_understanding": co.get("my_understanding", ""),
            "category": co.get("category", ""),
            "website": co.get("website", ""),
            "date_added": co.get("date_added", ""),
            "date_updated": co.get("date_updated", ""),
            "_embed_text": text_for_embedding,
        })

    # Frameworks (mutable entities)
    frameworks = load_json(FRAMEWORKS)
    for slug, fw in frameworks.items():
        parts = [fw.get("name", ""), fw.get("description", ""), fw.get("my_understanding", "")]
        text_for_embedding = ". ".join(p for p in parts if p)
        nodes.append({
            "id": slug,
            "type": "framework",
            "name": fw.get("name", slug),
            "description": fw.get("description", ""),
            "my_understanding": fw.get("my_understanding", ""),
            "date_added": fw.get("date_added", ""),
            "date_updated": fw.get("date_updated", ""),
            "_embed_text": text_for_embedding,
        })

    # Topics (mutable entities)
    topics = load_json(TOPICS)
    for slug, tp in topics.items():
        parts = [tp.get("name", ""), tp.get("description", ""), tp.get("my_understanding", "")]
        text_for_embedding = ". ".join(p for p in parts if p)
        nodes.append({
            "id": slug,
            "type": "topic",
            "name": tp.get("name", slug),
            "description": tp.get("description", ""),
            "my_understanding": tp.get("my_understanding", ""),
            "date_added": tp.get("date_added", ""),
            "date_updated": tp.get("date_updated", ""),
            "_embed_text": text_for_embedding,
        })

    return nodes


def cluster_nodes(embeddings: np.ndarray) -> np.ndarray:
    """Cluster embeddings using HDBSCAN. Returns cluster labels (-1 = noise)."""
    if not HDBSCAN_AVAILABLE or len(embeddings) < MIN_NODES_FOR_CLUSTERING:
        return -1 * np.ones(len(embeddings), dtype=int)

    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=MIN_CLUSTER_SIZE,
        min_samples=2,
        metric="euclidean",
    )
    return clusterer.fit_predict(embeddings)


def generate_cluster_label(texts: list[str]) -> str:
    """Generate a simple label from the most common words in cluster texts."""
    stop_words = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "must", "shall", "can", "to", "of", "in",
        "for", "on", "with", "at", "by", "from", "as", "into", "through",
        "during", "before", "after", "above", "below", "between", "under",
        "again", "further", "then", "once", "here", "there", "when", "where",
        "why", "how", "all", "each", "few", "more", "most", "other", "some",
        "such", "no", "nor", "not", "only", "own", "same", "so", "than",
        "too", "very", "just", "i", "me", "my", "myself", "we", "our", "you",
        "your", "he", "him", "his", "she", "her", "it", "its", "they", "them",
        "their", "what", "which", "who", "this", "that", "these", "those",
        "am", "and", "but", "if", "or", "because", "until", "while", "about",
        "against",
    }
    all_words = []
    for text in texts:
        words = text.lower().split()
        words = [w.strip(".,!?;:'\"()[]{}") for w in words]
        words = [w for w in words if w and w not in stop_words and len(w) > 2]
        all_words.extend(words)

    if not all_words:
        return "miscellaneous"

    counter = Counter(all_words)
    top_words = [word for word, _ in counter.most_common(3)]
    return " ".join(top_words)


def compute_connections(embeddings: np.ndarray, node_ids: list[str]) -> dict:
    """Compute similarity-based connections across the full corpus."""
    similarities = cosine_similarity(embeddings)
    connections = {}

    for i, node_id in enumerate(node_ids):
        sims = [
            (node_ids[j], float(similarities[i][j]))
            for j in range(len(node_ids))
            if i != j
        ]
        sims = [(nid, sim) for nid, sim in sims if sim >= SIMILARITY_THRESHOLD]
        sims.sort(key=lambda x: x[1], reverse=True)

        connections[node_id] = [
            {"target_id": nid, "similarity": round(sim, 3)}
            for nid, sim in sims[:MAX_CONNECTIONS_PER_NODE]
        ]

    return connections


def main():
    print("Loading all data sources...")
    nodes = build_node_list()

    if not nodes:
        print("No data to process.")
        save_json(OUTPUT, {
            "nodes": [],
            "clusters": [],
            "last_processed": datetime.utcnow().isoformat() + "Z",
        })
        return

    print(f"Processing {len(nodes)} nodes ({sum(1 for n in nodes if n['type'] == 'note')} notes, "
          f"{sum(1 for n in nodes if n['type'] != 'note')} entities)...")

    print("Loading embedding model...")
    model = SentenceTransformer(MODEL_NAME)

    print("Generating embeddings...")
    texts = [n["_embed_text"] for n in nodes]
    embeddings = model.encode(texts, show_progress_bar=False)

    print("Clustering...")
    cluster_labels = cluster_nodes(embeddings)

    # Build cluster metadata
    unique_clusters = set(int(c) for c in cluster_labels)
    skip_auto_labels = len(nodes) < MIN_NODES_FOR_CLUSTERING
    clusters = []
    for cluster_id in sorted(unique_clusters):
        cluster_texts = [texts[i] for i, c in enumerate(cluster_labels) if int(c) == cluster_id]
        auto_label = "uncategorized" if skip_auto_labels else generate_cluster_label(cluster_texts)
        clusters.append({
            "id": cluster_id,
            "auto_label": auto_label,
            "note_count": len(cluster_texts),
        })

    print("Computing connections...")
    node_ids = [n["id"] for n in nodes]
    connections = compute_connections(embeddings, node_ids)

    # Build output nodes (strip _embed_text, add cluster_id and connections)
    output_nodes = []
    for i, node in enumerate(nodes):
        out = {k: v for k, v in node.items() if not k.startswith("_")}
        out["cluster_id"] = int(cluster_labels[i])
        out["connections"] = connections[node["id"]]
        output_nodes.append(out)

    output = {
        "nodes": output_nodes,
        "clusters": clusters,
        "last_processed": datetime.utcnow().isoformat() + "Z",
    }
    save_json(OUTPUT, output)

    note_count = sum(1 for n in output_nodes if n["type"] == "note")
    entity_count = len(output_nodes) - note_count
    conn_count = sum(len(n["connections"]) for n in output_nodes)
    print(f"Done! {note_count} notes + {entity_count} entities, "
          f"{len(clusters)} clusters, {conn_count} connections.")


if __name__ == "__main__":
    main()
