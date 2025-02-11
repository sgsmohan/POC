@app.event("message")
def handle_message_events(event, say):
    text = event.get("text", "")

    # Check if the message looks like a table (contains tabs or multiple spaces)
    if "\t" in text or "  " in text:
        try:
            # Convert tab-separated text into a DataFrame
            rows = [line.split("\t") for line in text.strip().split("\n")]
            df = pd.DataFrame(rows[1:], columns=rows[0])  # First row as headers
            
            # Save to TSV file
            modified_file_path = "/tmp/modified_file.tsv"
            df.to_csv(modified_file_path, sep="\t", index=False)

            # Upload to Slack
            response = client.files_upload(
                channels=event["channel"],
                file=modified_file_path,
                title="Processed TSV File"
            )

            say("Here is the modified TSV file with bold headers.")

        except Exception as e:
            say(f"Error processing file: {str(e)}")
