import discord
import asyncio
import chatlogging
import logging
import command_manager

client = discord.Client()

#Display useful info in terminal
logging.basicConfig(level=logging.INFO)

@client.event
async def on_message(message):
    chatlogging.cmdlog(message)
    command_response = command_manager.return_command_response(message)
    if command_response is not None:
        await client.send_message(message.channel, command_response)

@client.event
async def on_ready():
    chatlogging.cmdlog('', 'login')
            

key = input('Please enter bot token: ')
client.run(key)
