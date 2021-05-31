import os
import discord
import requests
import json
import random

client=discord.Client()

sad_words=['sad','depressed','help','cheer','unhappy']

starter_quotes=['Cheer up!',
"Hang in there",
"You are a great person"]


def get_quote():
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q']+" -"+json_data[0]['a']
  return{quote}


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hey there')

  if message.content.startswith('$inspire'):
    quote=get_quote()
    await message.channel.send(quote)

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(starter_quotes))
  
client.run(os.getenv('TOKEN'))

