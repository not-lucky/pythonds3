from discord import SyncWebhook

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1097188200809779311/WlTTRZExuMtIppOZ6gJUh8YTmn61DAK6wG1xLevPMunVodJSDPo1Kv3zvzHA-gX0fniR")
webhook.send("Hello World")