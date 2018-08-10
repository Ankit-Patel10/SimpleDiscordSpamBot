import discord
import pickle
import random
import asyncio
import os
import time

token = ("Enter Token Here")
client = discord.Client()
howmanymessages = int(input("How many different messages:"))
delay = int(input("Delay in ms:"))
list = []
for x in range(0, howmanymessages):
    txt = str(input("Text to spam:"))
    list[x] = txt
spamamt = int(input("The amount of message:"))
invitelink = str(input("Channel invite link:"))

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.startswith("+raidhere"):
        for x in range(0, spamamt):
            time.sleep(1)
            for i in range(0, howmanymessages):
                await client.send_message(message.channel, list[i])
                time.sleep(delay)

@client.event
async def on_ready():
    await client.accept_invite(invitelink)

client.run(token, bot=False)
