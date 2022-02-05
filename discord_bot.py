# bot.py
import os
import io
import getimagerss.py
import discord
import subprocess
import praw
import wget
import urllib
import mimetypes
import asyncio
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('CHANNEL')
SERVER = os.getenv('DISCORD_GUILD')
REDDIT_ID = os.getenv('REDDIT_ID')
REDDIT_SECRET = os.getenv('REDDIT_SECRET')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
client.run(TOKEN)

def tipe(link, strict=True):
    link_type, _ = mimetypes.guess_type(link)
    if link_type is None and strict:
        link_type = "text/html"
    return link_type

async def down(z, str):
    r = wget.download(z, str)
    await send_image(str)
    
def remove_file(str1):
    if os.path.exists(str1):
        os.remove(str1)
    else:
        print("The file does not exist") 

async def send_image(str):
    await CHANNEL.send(file=discord.File(str))
    
reddit_read_only = praw.Reddit(client_id=REDDIT_SECRET,		         # your client id
							client_secret=REDDIT_ID,	             # your client secret
							user_agent="Mozilla")	                 # your user agent

subreddit = reddit_read_only.subreddit("hentai")

for post in subreddit.stream.submissions():                                     
    if ( tipe(post.url) != "text/html"):  #Sorts out the wrong image extentions                                                     
        print(post.url)
        down(post.url,"x.jpg")
        print('Image Successfully Downloaded', post.url)
        asyncio.run(down(post.url,"x.jpg")) #Send Image
        remove_file("x.jpg")


