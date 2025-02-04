using System;
using System.Threading.Tasks;
using Microsoft.Azure.WebJobs;
using Microsoft.Extensions.Logging;
using SendGrid;
using SendGrid.Helpers.Mail;

public static class SendEmailFunction
{
    [FunctionName("SendEmailFunction")]
    public static async Task Run(
        [TimerTrigger("0 0 9 * * *")] TimerInfo myTimer, 
        ILogger log)
    {
        log.LogInformation($"Function executed at: {DateTime.UtcNow}");

        // SendGrid API Key (Use Azure Key Vault for security)
        string apiKey = Environment.GetEnvironmentVariable("SendGridApiKey");
        string fromEmail = "your-email@example.com";
        string toEmail = "recipient@example.com";

        var client = new SendGridClient(apiKey);
        var msg = new SendGridMessage()
        {
            From = new EmailAddress(fromEmail, "Your Name"),
            Subject = "Scheduled Email",
            PlainTextContent = "Hello, this is a test email sent by Azure Functions!",
            HtmlContent = "<strong>Hello, this is a test email sent by Azure Functions!</strong>"
        };
        msg.AddTo(new EmailAddress(toEmail));

        var response = await client.SendEmailAsync(msg);
        log.LogInformation($"Email sent with status code: {response.StatusCode}");
    }
}
