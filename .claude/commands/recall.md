Search the AI intelligence database for entries matching a query.

User input: $ARGUMENTS

## Your task

1. Read all three files: `data/companies.json`, `data/frameworks.json`, `data/topics.json`.

2. Treat the input as a free-text search query. Search case-insensitively across ALL text fields:
   - Companies: name, description, my_understanding, category, business_model, gtm_hacks, sources, key_employees names/roles, links
   - Frameworks: name, description, my_understanding, key_principles
   - Topics: name, description, my_understanding, related_companies

3. Rank results by relevance:
   - Exact match on name or slug → highest
   - Match in description or my_understanding → medium
   - Match in other fields → lower

4. Display each match as:

   **[Company / Framework / Topic]** `<slug>`
   **Name:** <name>
   **Category:** <category> *(companies only)*
   **Description:** <description>
   **My Understanding:** <my_understanding>
   *(plus other populated fields relevant to the query)*

5. If the query is a question (e.g. "what are RAG companies?"), interpret it semantically — match on concepts, not just literals.

6. Show at most 10 results. If more exist, note the total count and suggest a narrower query.

7. If no matches found, say so and suggest `/list` to browse all entries.

8. Do not modify any files — read-only.
