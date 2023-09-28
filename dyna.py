import requests
import json
import time

# Replace with your Dynatrace API token
api_token = 'YOUR_API_TOKEN'

# Replace with your organization-managed Dynatrace API endpoint
api_endpoint = 'https://<your-environment-ID>.live.dynatrace.com/e/<your-environment-ID>/api/v2/metrics/ingest'

headers = {
    'Authorization': f'Api-Token {api_token}',
    'Content-Type': 'application/json',
}

# Example metric data (replace with your own data)
metric_data = [
    {
        "metricKey": "custom.my_metric",
        "dimensions": [
            {
                "key": "environment",
                "value": "production"
            }
        ],
        "timestamp": int(time.time()) * 1000,  # Current timestamp in milliseconds
        "value": 42
    }
]

payload = json.dumps(metric_data)

response = requests.post(api_endpoint, headers=headers, data=payload)

if response.status_code == 202:
    print("Metric data sent successfully.")
else:
    print(f"Failed to send metric data. Status code: {response.status_code}")
    print(response.text)
