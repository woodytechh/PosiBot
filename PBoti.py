import discord
import os
import requests
import json
import random

intents = discord.Intents.default()
intents.message_content = True 

client = discord.Client(intents=intents)

sad_words = [ ... ]  # (Keep as-is)
starter_encouragements = [ ... ]  # (Keep as-is)
thank_you_words = [ ... ]  # (Keep as-is)
thank_you_replies = [ ... ]  # (Keep as-is)

def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()  # make it case-insensitive

    if msg.startswith('$inspire'):
        quote = getQuote()
        await message.channel.send(quote)
        
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
        
    if any(word in msg for word in thank_you_words):
        await message.channel.send(random.choice(thank_you_replies))

# Run the bot
client.run(os.getenv('DISCORD_TOKEN'))
