# client id 705275933912989736
# token NzA1Mjc1OTMzOTEyOTg5NzM2.XqpW4g.v1WoQDPsfOV4rl0A6-muDad9Z5w
# permission integer 67584
# url https://discordapp.com/oauth2/authorize?client_id=705275933912989736&scope=bot&permissions=67584

import discord
import rpy2
from rpy2.robjects import r
client =discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    msg=message.content
    if msg[0]==">":
        msg=msg[1:]
    msg=msg.replace("\n+","\n")
    msg= msg.replace("\n>","\n")
    if str(message.author)[:6]=="Rython":
        return
    try:
        msg=str(r(msg))
    except rpy2.rinterface_lib.embedded.RRuntimeError:
        msg = "A runtime error occured (In your code)"
    await message.channel.send(msg)

client.run("NzA1Mjc1OTMzOTEyOTg5NzM2.XqpW4g.v1WoQDPsfOV4rl0A6-muDad9Z5w")