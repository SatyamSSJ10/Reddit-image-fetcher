#Requesting Reddit API to get image link and then downloading the image through python

import os
import praw
import wget
import mimetypes
import gc
import pandas as pd

def tipe(link, strict=True):
    link_type, _ = mimetypes.guess_type(link)
    if link_type is None and strict:
        link_type = "text/html"
    return link_type

def down(z, str):
    r = wget.download(z, str)	# Parameter String, String
    
reddit_data = praw.Reddit(client_id="Client ID",		         # your client id \ Parameter String
			       client_secret="Client Secret",	         # your client secret \ Parameter String
			       user_agent="Useragent for Reddit")	 # your user agent \ Parameter String

subreddit = reddit_data.subreddit("subreddit_name") #Parameter String

for post in subreddit.stream.submissions():     #Fethces New Submission                                
    if ( tipe(post.url) != "text/html"):                                                  
        print(post.url)
        down(post.url,"download.jpg")
        print('Image Successfully Downloaded', post.url)
	del post
	gc.collect()
  
