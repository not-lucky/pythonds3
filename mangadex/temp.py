import discord
import requests
import random

# # list of image urls and messages
# images = ['https://i.imgur.com/R33SQ0R.jpg', 'https://i.imgur.com/tXTLBfe.jpg']
# messages = ['Hello!', 'How are you?']

# # loop through list and send embeds
# for i in range(len(images)):
#     # generate random color for each embed
#     color = random.randint(0, 0xFFFFFF)

#     embed = discord.Embed(title="Embed Title",
#                           description=messages[i],
#                           color=color)
#     embed.set_image(url=images[i])

#     webhook.send(embed=embed)

webhook = discord.SyncWebhook.from_url(
    "https://discord.com/api/webhooks/1097188200809779311/WlTTRZExuMtIppOZ6gJUh8YTmn61DAK6wG1xLevPMunVodJSDPo1Kv3zvzHA-gX0fniR"
)
# Generate a list of random messages and images
messages = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium."
]
images = ["https://picsum.photos/200/300", "https://picsum.photos/300/200"]

# Split the messages into chunks of 2000 characters or less
message_chunks = [messages[i:i + 2] for i in range(0, len(messages), 2)]

# Create and send an embed for each message chunk
for chunk in message_chunks:
    embed = discord.Embed()
    embed.description = "test"
    embed = discord.Embed(title='Embed Title',
                          description='Embed Description',
                          color=discord.Color.blue())

    # First field
    embed.add_field(name='Field 1 Name', value='Field 1 Value', inline=False)

    # Second field
    embed.add_field(name='Field 2 Name', value='Field 2 Value', inline=False)

    # Third field
    embed.add_field(name='Field 3 Name', value='Field 3 Value', inline=False)

    # Fourth field
    embed.add_field(name='Field 4 Name', value='Field 4 Value', inline=False)

    # for i, message in enumerate(chunk):
    #     embed.add_field(name=f"Message {i+1}", value=message, inline=False)
    #     # embed.set_image(url=random.choice(images))
    webhook.send(embed=embed)
