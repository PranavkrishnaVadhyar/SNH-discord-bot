import discord
import os
import requests
import json
import random


client = discord.Client(intents=discord.Intents.all())

data = ['depressed','sad','down','angry','desperate','lonely','unhappy']

responese = ['Heyy you are the best','Dont worry. Everything will be ok ','You are the best developer I know','Just think of the good memories you had','Just think about the good things in your life']

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "-" + json_data[0]['a']
    return quote
    
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
@client.event

async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith('inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        
        
        
    if any(word in message.content for word in data):
            
            await message.channel.send(random.choice(responese))

client.run(os.getenv('TOKEN'))
