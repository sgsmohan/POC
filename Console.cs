using System;
using System.Linq;
using System.Threading.Tasks;
using SlackNet;
using SlackNet.Events;
using SlackNet.WebApi;

class Program
{
    static async Task Main()
    {
        var slackApi = new SlackApiClient("xoxb-your-bot-token"); // Replace with your bot token
        var eventHandler = new SlackEventHandler(slackApi);
        
        var slackReceiver = new SlackEndpoint(eventHandler);
        await slackReceiver.ListenAsync(port: 3000); // Run server on port 3000
    }
}

public class SlackEventHandler : IEventHandler<MessageEvent>
{
    private readonly ISlackApiClient _slackApi;
    private readonly string _botUserId;

    public SlackEventHandler(ISlackApiClient slackApi)
    {
        _slackApi = slackApi;
        _botUserId = slackApi.Auth.Test().Result.UserId; // Get bot's user ID
    }

    public async Task Handle(MessageEvent slackEvent)
    {
        // Check if the bot is mentioned and message contains "hi" or "hello"
        if (slackEvent.Text.Contains($"<@{_botUserId}>") &&
            (slackEvent.Text.Contains("hi", StringComparison.OrdinalIgnoreCase) ||
             slackEvent.Text.Contains("hello", StringComparison.OrdinalIgnoreCase)))
        {
            await _slackApi.Chat.PostMessage(slackEvent.Channel, "Hello! 😊");
        }
    }
}
