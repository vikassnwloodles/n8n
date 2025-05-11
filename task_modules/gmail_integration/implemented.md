### Workflow

1. Fetched Emails
    - Got sent emails (last 24 hours)
    - Got received emails (last 72 hours)

2. Cleaned & Tagged Data
    - Kept only important email fields
    - Added labels:
        - "sent" for sent emails
        - "received" for received emails

3. Combined & Split Data
    - Put all emails together in one list
    - Cleaned text using regex
        - Removed invisible Unicode characters
        - Stripped URLs and web links
        - Normalized excessive newlines and whitespace
        - Trimmed trailing spaces
    - Split into smaller chunks (to fit GPT limits)

4. AI Processing
    - Sent each chunk to GPT for summaries
    - Got back one summary per chunk

5. Final Report
    - Combined all summaries together
    - Sent to GPT to make one morning brief
