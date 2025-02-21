using SlackNet;
using SlackNet.Blocks;
using SlackNet.WebApi;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var slackApiClient = new SlackApiClient("xoxb-your-token");

        // Sample table data
        var tableData = new List<(string Name, int Age, string Role)>
        {
            ("Alice", 30, "Developer"),
            ("Bob", 28, "Designer"),
            ("Charlie", 35, "Manager")
        };

        // Construct header row
        var blocks = new List<Block>
        {
            new SectionBlock
            {
                Fields = new List<TextObject>
                {
                    new TextObject { Type = "mrkdwn", Text = "*Name*" },
                    new TextObject { Type = "mrkdwn", Text = "*Age*" },
                    new TextObject { Type = "mrkdwn", Text = "*Role*" }
                }
            },
            new DividerBlock()
        };

        // Construct table rows
        foreach (var row in tableData)
        {
            blocks.Add(new SectionBlock
            {
                Fields = new List<TextObject>
                {
                    new TextObject { Type = "mrkdwn", Text = row.Name },
                    new TextObject { Type = "mrkdwn", Text = row.Age.ToString() },
                    new TextObject { Type = "mrkdwn", Text = row.Role }
                }
            });
        }

        // Send the message
        await slackApiClient.Chat.PostMessage(new Message
        {
            Channel = "your-channel-id",
            Blocks = blocks
        });

        Console.WriteLine("Table sent to Slack!");
    }
}
