Add or update a company entry in the AI intelligence database.

User input: $ARGUMENTS

## Your task

1. Run `git pull` to sync the latest data before making changes.

2. Read `data/companies.json`.

3. Generate a slug from the company name: lowercase, spaces and special characters replaced with hyphens, no leading/trailing hyphens. Example: "Anysphere (Cursor)" → "anysphere-cursor".

4. Check if an entry with that slug already exists:
   - **Exists**: update. Preserve all existing fields. Only overwrite fields explicitly mentioned in the user input. Set `date_updated` to today (YYYY-MM-DD). Do NOT change `date_added`.
   - **Does not exist**: create. Set both `date_added` and `date_updated` to today.

5. Parse the user's input and populate as many fields as possible. Fields are delimited by semicolons (`;`). Commas within a field are part of the text, not delimiters. Leave fields as `""` or `[]` if information is not provided — never invent data.

   Fields:
   - `slug` (string) — generated as above
   - `name` (string) — canonical display name
   - `description` (string) — factual 1-2 sentence description
   - `my_understanding` (string) — the user's personal take, verbatim if quoted
   - `category` (string) — e.g. "coding tools", "agent frameworks", "foundation models", "data infrastructure", "AI ops", "vertical AI", "hardware", "research"
   - `website` (string) — primary URL
   - `links` (array of strings) — secondary URLs
   - `business_model` (string) — pricing and monetisation model
   - `gtm_hacks` (string) — growth and go-to-market observations
   - `key_employees` (array of `{ "name": string, "role": string }`) — notable people
   - `sources` (array of strings) — where the user heard about this
   - `date_added` (string, ISO date)
   - `date_updated` (string, ISO date)

6. Write the updated `data/companies.json` back with 2-space indentation.

7. Confirm: slug, create or update, which fields were populated or changed.

8. Run `git add data/companies.json`, then commit with message "Add/Update <company name> in AI intelligence database", then `git push`.

## Notes
- Never delete existing fields on update — only add or overwrite what the user mentions.
- If the input company name is close to an existing slug, confirm with the user before creating a duplicate.
