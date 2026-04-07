Add or update a note in the second brain.

User input: $ARGUMENTS

## Your task

1. Run `git pull` to sync the latest data before making changes.

2. Read `data/notes_raw.json`.

3. Parse the user's input as the note content. The input is free-form text — treat it as the note body.
   - If the input contains a semicolon, treat the text before the first semicolon as the `subject` and the rest as the `text`.
   - If no semicolon, generate a short subject (5-7 words) summarizing the note, and use the full input as `text`.

4. Create a new note object:
   - `id`: Generate a UUID v4
   - `text`: The note body
   - `subject`: The subject/title
   - `timestamp`: Current time in ISO 8601 format (e.g. "2026-04-07T10:30:00.000Z")
   - `source`: `"manual"`

5. Append the new note to the `notes` array in `data/notes_raw.json`. Do NOT modify or delete any existing notes — this is append-only.

6. Write the updated `data/notes_raw.json` back with 2-space indentation.

7. Confirm: show the subject, first 100 chars of text, and timestamp.

8. Run `git add data/notes_raw.json`, then commit with message "Add note: <subject>", then `git push`.

## Notes
- Never modify or delete existing notes. Notes are immutable and append-only.
- Never invent or embellish the note content — use the user's words verbatim.
- The `source` field is always `"manual"` for notes added via this command (as opposed to `"email"` for notes captured via the email flow).
