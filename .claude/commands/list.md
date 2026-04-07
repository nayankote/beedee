List entries in the AI intelligence database.

User input: $ARGUMENTS

## Your task

1. Parse the input:
   - Empty or "all" → list everything from all four files
   - "companies" or a category name (e.g. "coding tools") → list from companies.json, filtered by category if specific
   - "frameworks" → list from frameworks.json only
   - "topics" → list from topics.json only
   - "notes" → list from notes_raw.json only

2. Read the relevant file(s).

3. Display a scannable list:

   **Companies**
   - `<slug>` — **<name>** | <category> | <website> | Added: <date_added>

   **Frameworks**
   - `<slug>` — **<name>** | Added: <date_added>

   **Topics**
   - `<slug>` — **<name>** | Related companies: <count> | Added: <date_added>

   **Notes**
   - `<first 8 chars of id>` — **<subject or first 40 chars of text>** | <timestamp date only> | <source>

4. End with a summary count, e.g. "3 companies, 1 framework, 2 topics, 13 notes."

5. If a file has no entries, say "No <type> entries yet — use /add-<type> to add one."

6. Do not modify any files — read-only.
