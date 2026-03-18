Add or update a framework entry in the AI intelligence database.

User input: $ARGUMENTS

## Your task

1. Read `data/frameworks.json`.

2. Generate a slug: lowercase, spaces and special characters replaced with hyphens. Example: "Chain-of-Thought" → "chain-of-thought".

3. Check if an entry with that slug already exists:
   - **Exists**: update. Preserve all existing fields. Only overwrite fields explicitly mentioned. Set `date_updated` to today (YYYY-MM-DD). Do NOT change `date_added`.
   - **Does not exist**: create. Set both dates to today.

4. Parse the input and populate these fields. Leave as `""` or `[]` if not provided — never invent data.

   Fields:
   - `slug` (string)
   - `name` (string)
   - `description` (string) — factual summary
   - `my_understanding` (string) — the user's personal interpretation or mental model
   - `key_principles` (array of strings) — core ideas, techniques, or rules
   - `date_added` (string, ISO date)
   - `date_updated` (string, ISO date)

5. Write the updated `data/frameworks.json` back with 2-space indentation.

6. Confirm: slug, create or update, which fields changed.
