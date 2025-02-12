using System;
using System.Linq;
using System.Threading.Tasks;
using SlackNet;
using SlackNet.Events;
using SlackNet.SocketMode;
using SlackNet.WebApi;

class Program
{
    static async Task Main()
    {
        string botToken = "xoxb-your-bot-token"; // Replace with your bot token
        string appToken = "xapp-your-app-token"; // Replace with your App-Level Token (Socket Mode enabled)

        var slackServices = new SlackServiceBuilder()
            .UseApiToken(botToken)
            .UseSocketMode(appToken);

        using var slack = slackServices.GetApiClient();
        var botUserId = (await slack.Auth.Test()).UserId; // Get Bot's User ID

        using var socketModeClient = slackServices.GetSocketModeClient();
        socketModeClient.OnEvent<MessageEvent>(async (msg) =>
        {
            // Check if bot is mentioned and message contains "hi" or "hello"
            if (msg.Text.Contains($"<@{botUserId}>") &&
                (msg.Text.Contains("hi", StringComparison.OrdinalIgnoreCase) ||
                 msg.Text.Contains("hello", StringComparison.OrdinalIgnoreCase)))
            {
                await slack.Chat.PostMessage(msg.Channel, "Hello! 😊");
            }
        });

        Console.WriteLine("Bot is listening... Press Ctrl+C to exit.");
        await socketModeClient.Connect();
    }
}
