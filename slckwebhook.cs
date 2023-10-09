

using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string webhookUrl = "YOUR_WEBHOOK_URL_HERE"; // Replace with your actual webhook URL

        // Create an HttpClient to send the POST request
        using (var httpClient = new HttpClient())
        {
            // Create a JSON payload for the Slack message
            var payload = new
            {
                text = "Hello, Slack! This is a test message from your C# console app."
            };

            // Serialize the payload to JSON
            var jsonPayload = Newtonsoft.Json.JsonConvert.SerializeObject(payload);

            // Create a StringContent with JSON data
            var content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");

            // Send the POST request to the Slack webhook URL
            var response = await httpClient.PostAsync(webhookUrl, content);

            // Check if the request was successful
            if (response.IsSuccessStatusCode)
            {
                Console.WriteLine("Message sent successfully!");
            }
            else
            {
                Console.WriteLine($"Error: {response.StatusCode} - {await response.Content.ReadAsStringAsync()}");
            }
        }
    }
}
