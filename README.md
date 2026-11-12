# Telegram Webhook Setup

This project contains a simple Python script for registering a Telegram bot webhook with the Telegram Bot API.

It is useful when you want Telegram to send updates to your own HTTPS endpoint, such as a Cloudflare Worker, FastAPI app, or any custom webhook server.

## What the script does

The script:

- asks for your Telegram bot token
- asks for a webhook secret
- sends a `POST` request to Telegram's `setWebhook` API
- configures the webhook URL for your bot

The webhook URL is currently defined in the script as:

```python
worker_url = "https://amanu-ai.amanlasta9.workers.dev/telegram"
```

You should replace this with your own deployed webhook endpoint before using it.

## Prerequisites

- Python 3 installed
- A Telegram bot created with BotFather
- A valid HTTPS webhook endpoint already deployed and ready to receive Telegram updates
- A secret token you want to use for verifying incoming requests

## Create a Telegram bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Follow the prompts to choose a name and username
4. Copy the bot token that BotFather gives you

## Configure the script

Open `setup_webhook.py` and update the webhook URL if needed:

```python
worker_url = "https://your-domain.example.com/telegram"
```

Then run:

```bash
python setup_webhook.py
```

On execution, the script will prompt for:

- `Enter Telegram bot token:`
- `Enter WEBHOOK_SECRET:`

## Example

```bash
python setup_webhook.py
Enter Telegram bot token: 123456:ABCDEF
Enter WEBHOOK_SECRET: my-secure-secret
```

The script then sends a request like this to Telegram:

```http
POST https://api.telegram.org/bot<token>/setWebhook
```

with JSON data similar to:

```json
{
  "url": "https://your-domain.example.com/telegram",
  "secret_token": "my-secure-secret"
}
```

## Why use a webhook?

A webhook lets Telegram push updates to your app instead of constantly polling the Telegram API. This is more efficient and is the usual setup for bots that react to messages, commands, and events in real time.

## Security notes

- Keep your bot token private
- Use a strong secret value for `WEBHOOK_SECRET`
- Only use HTTPS endpoints
- Validate the secret on your receiving server before processing incoming Telegram requests

## Troubleshooting

### Telegram responds with an error

The script prints Telegram error details if the request fails. Common causes include:

- invalid bot token
- bad webhook URL
- your server not reachable over HTTPS
- incorrect secret handling

### Connection error

If the script shows a connection error, check:

- your internet connection
- whether the webhook URL is reachable
- whether the endpoint is actually running

## Notes

This script only configures the Telegram webhook. Your backend server is responsible for:

- receiving webhook requests
- validating the `secret_token`
- processing Telegram updates
- responding appropriately

## License

This project is provided for personal or internal use. Add your preferred license if you plan to share it publicly.
