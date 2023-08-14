import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def get_channel_names():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from the Slack app.
    slack_token = "YOUR_BOT_TOKEN"
    client = WebClient(token=slack_token)

    try:
        response = client.conversations_list()
        channels = response["channels"]

        channel_names = [channel["name"] for channel in channels]
        return channel_names
    except SlackApiError as e:
        print(f"Error fetching channel names: {e}")
        return []

if __name__ == "__main__":
    channel_names = get_channel_names()

    if channel_names:
        print("List of channel names:")
        for name in channel_names:
            print(name)
    else:
        print("No channel names found.")
