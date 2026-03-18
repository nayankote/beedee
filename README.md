# beedee

Brain Dump, records information about startups, frameworks, topics that I encounter on the daily. Inspired by my friend [Vishwajit Sasi](https://v7t.space/about) at Accel.

## Commands

| Command | Example | Description |
|---|---|---|
| `/add-company` | `/add-company Anthropic, foundation models, anthropic.com, Dario Amodei is CEO, makes Claude` | Add or update a company |
| `/add-framework` | `/add-framework Chain-of-Thought, prompting technique where model reasons step by step before answering` | Add or update a framework |
| `/add-topic` | `/add-topic Vibe Coding, AI-assisted coding without reading the code, related to Anysphere` | Add or update a topic |
| `/recall` | `/recall RAG companies` or `/recall what do I know about Anthropic` | Semantic search across all entries |
| `/list` | `/list all` or `/list companies` or `/list coding tools` | Browse entries |

## Data

All data lives in `data/` as flat JSON objects keyed by slug:
- `data/companies.json`
- `data/frameworks.json`
- `data/topics.json`

Slugs are auto-generated: `Anysphere (Cursor)` → `anysphere-cursor`. They're used as stable cross-references (e.g. `related_companies` in topics stores company slugs).

## Company fields

| Field | Type | Description |
|---|---|---|
| `name` | string | Display name |
| `description` | string | Factual summary |
| `my_understanding` | string | Your personal take |
| `category` | string | e.g. "coding tools", "agent frameworks", "foundation models" |
| `website` | string | Primary URL |
| `links` | array | Secondary URLs |
| `business_model` | string | Pricing / monetisation |
| `gtm_hacks` | string | Growth observations |
| `key_employees` | array | `[{ "name": "...", "role": "..." }]` |
| `sources` | array | Where you heard about them |
