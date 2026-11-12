
import json
import urllib.request
import urllib.error
import getpass

bot_token = getpass.getpass("Enter Telegram bot token: ")
secret = getpass.getpass("Enter WEBHOOK_SECRET: ")


worker_url = "https://amanu-ai.amanlasta9.workers.dev/telegram"

data = {
    "url": worker_url,
    "secret_token": secret
}

request = urllib.request.Request(
    f"https://api.telegram.org/bot{bot_token}/setWebhook",
    data=json.dumps(data).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(request) as response:
        print(response.read().decode())

except urllib.error.HTTPError as error:
    print("Telegram error details:")
    print(error.read().decode())

except Exception as error:
    print("Connection error:", error)
