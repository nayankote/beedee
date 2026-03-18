List entries in the AI intelligence database.

User input: $ARGUMENTS

## Your task

1. Parse the input:
   - Empty or "all" → list everything from all three files
   - "companies" or a category name (e.g. "coding tools") → list from companies.json, filtered by category if specific
   - "frameworks" → list from frameworks.json only
   - "topics" → list from topics.json only

2. Read the relevant file(s).

3. Display a scannable list:

   **Companies**
   - `<slug>` — **<name>** | <category> | <website> | Added: <date_added>

   **Frameworks**
   - `<slug>` — **<name>** | Added: <date_added>

   **Topics**
   - `<slug>` — **<name>** | Related companies: <count> | Added: <date_added>

4. End with a summary count, e.g. "3 companies, 1 framework, 2 topics."

5. If a file has no entries, say "No <type> entries yet — use /add-<type> to add one."

6. Do not modify any files — read-only.
