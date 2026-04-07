Process all beedee data and push the visualization to the personal website.

Run this whenever you want to update the graph on nayankote.com/notes.

## Your task

1. Pull the latest data from beedee remote (in case email notes have arrived):
   ```
   git pull
   ```

2. Run the processing pipeline:
   ```
   cd /Users/nnandan/Projects/beedee && python scripts/process_brain.py
   ```
   This generates `data/brain_processed.json` with embeddings and cross-connections for all notes + entities.

3. Copy the processed output to the personal website repo:
   ```
   cp /Users/nnandan/Projects/beedee/data/brain_processed.json /Users/nnandan/Projects/personal_website/notes/notes_processed.json
   ```

4. Commit and push beedee:
   ```
   git add data/brain_processed.json
   git commit -m "Update processed brain data"
   git push
   ```

5. Commit and push the personal website:
   ```
   cd /Users/nnandan/Projects/personal_website
   git add notes/notes_processed.json
   git commit -m "Update brain visualization data from beedee"
   git push
   ```

6. Confirm: how many notes, entities, and connections were processed. Mention that nayankote.com/notes will update shortly (GitHub Pages deploy).
