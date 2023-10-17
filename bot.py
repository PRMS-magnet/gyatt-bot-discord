# this example requires the 'message_content' intent.

import token
import discord
import random
from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")

attention = ["gyatt","GYATT","🍑","GYATT!","Gyatt","Gyatt!","gyatt!"]
response = ["Gyatt!","Gyatt!","Damn!"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#log in check
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

#main loop
@client.event
async def on_message(message):
    #cancel if the message is by the bot
    if message.author == client.user:
        return
    
    #random response
    sendmsg = random.choice(response)
    #check messages and then send message
    [await message.channel.send(sendmsg) for word in message.content.split(' ') if word in attention]


client.run(TOKEN)