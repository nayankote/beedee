Add or update a topic entry in the AI intelligence database.

User input: $ARGUMENTS

## Your task

1. Read `data/topics.json` and `data/companies.json`.

2. Generate a slug: lowercase, spaces replaced with hyphens, special characters removed. Example: "Vibe Coding" → "vibe-coding".

3. Check if an entry with that slug already exists in topics.json:
   - **Exists**: update. Preserve existing fields. Only overwrite what the user mentions. Set `date_updated` to today (YYYY-MM-DD). Do NOT change `date_added`.
   - **Does not exist**: create. Set both dates to today.

4. Parse the input and populate these fields. Leave as `""` or `[]` if not provided — never invent data.

   Fields:
   - `slug` (string)
   - `name` (string)
   - `description` (string) — objective description
   - `my_understanding` (string) — user's personal perspective
   - `related_companies` (array of strings) — company slugs from companies.json. Convert any company names the user mentions to slugs. Check companies.json to verify each slug exists; if a company isn't in the database yet, still add the expected slug and warn the user.
   - `date_added` (string, ISO date)
   - `date_updated` (string, ISO date)

5. Write the updated `data/topics.json` back with 2-space indentation.

6. Confirm: slug, create or update, fields populated, and any unresolved company slug warnings.
