import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_message(channel, message):
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from the Slack app.
    slack_token = "YOUR_BOT_TOKEN"
    client = WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(channel=channel, text=message)
        print(f"Message sent: {response['ts']}")
    except SlackApiError as e:
        print(f"Error sending the message: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_CHANNEL_ID' with the actual channel ID (e.g., 'C01234567').
    channel_id = "YOUR_CHANNEL_ID"
    message_to_send = "Hello, this is a message from the Python script!"
    send_slack_message(channel=channel_id, message=message_to_send)
