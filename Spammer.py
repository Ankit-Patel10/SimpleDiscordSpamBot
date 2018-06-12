import discord
import pickle
import random
import asyncio
import os
import time

token = ("enter ur token here")
client = discord.Client()
howmanymessages = int(input("plz enter how many different messages you want:"))
delay = int(input("plz enter the delay"))
list = []
for x in range(0, howmanymessages):
    raidtxt = str(input("plz enter in spam text:"))
    list[x] = raidtxt
spamamt = int(input("plz enter the amt of spam u want:"))
invitelink = str(input("plz enter an invite link for server ud like to raid: "))

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
