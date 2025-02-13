using System;
using System.Threading.Tasks;
using SlackNet;
using SlackNet.Events;
using SlackNet.WebApi;

class Program
{
    static async Task Main()
    {
        // Replace with your actual Slack bot token
        string botToken = "xoxb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        string channelId = "C06C7TH631Z"; // Replace with your Slack channel ID

        var slackService = new SlackServiceBuilder()
            .UseApiToken(botToken)
            .GetApiClient();

        var eventHandler = new SlackEventHandler(slackService, channelId);

        Console.WriteLine("Listening for messages... Press Ctrl+C to stop.");
        await eventHandler.Listen();
    }
}

class SlackEventHandler
{
    private readonly ISlackApiClient _slackApiClient;
    private readonly string _channelId;

    public SlackEventHandler(ISlackApiClient slackApiClient, string channelId)
    {
        _slackApiClient = slackApiClient;
        _channelId = channelId;
    }

    public async Task Listen()
    {
        var eventHandler = new EventHandler();

        eventHandler.OnMessageReceived(async message =>
        {
            if (message.Text.Contains("hi", StringComparison.OrdinalIgnoreCase))
            {
                await Respond(message.Channel);
            }
        });

        await Task.Delay(-1); // Keep running
    }

    private async Task Respond(string channel)
    {
        await _slackApiClient.Chat.PostMessage(new Message
        {
            Text = "Hi",
            Channel = channel
        });
    }
}
