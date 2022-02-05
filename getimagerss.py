#Requesting Reddit API to get image link and then downloading the image through python
#Link file for discord_bot.py
import os
import subprocess
import praw
import wget
import urllib
import mimetypes
import pandas as pd

def tipe(link, strict=True):
    link_type, _ = mimetypes.guess_type(link)
    if link_type is None and strict:
        link_type = "text/html"
    return link_type

def down(z, str):
    r = wget.download(z, str)

def remove_file(str1):
    if os.path.exists(str1):
        os.remove(str1)
    else:
        print("The file does not exist") 
        
reddit_read_only = praw.Reddit(client_id="FROM ENV",		         # your client id
				client_secret="FROM ENV",	     # your client secret
				user_agent="FROM ENV")	                         # your user agent

subreddit = reddit_read_only.subreddit("hentai")

for post in subreddit.stream.submissions():                                     
    if ( tipe(post.url) != "text/html"):  #if (tipe(post.url) != 'None'):                                                         
        print(post.url)
        down(post.url,"x.jpg")
        print('Image Successfully Downloaded', post.url)
        #POST IMAGE TO DISCORD
        remove_file("x.jpg")
        
        
        
#async def announce(CHANNEL):
#await channel.send(file=discord.File('*.png'))       #Sending File Message ETC.




