# There's a chance you could get banned/shadowed with this bot, but it also may just be a result of not sleeping 
# long enough between comments. 
# It can also be configured to reply to only the newest comment, if a user doesn't comment often. 
# I will likely release more updated versions intended to respond if a keyword is triggered and save responded-to posts later,
# but as of now, this is only meant as a basic structural function 

import praw
import random
from time import sleep

a = input("What's your client_id? ")
b = input("What's your client secret? ")
c = input("What's your username? ")
d = input("What's your password? ")


reddit = praw.Reddit(client_id = str(a), 
                     client_secret = str(b),
                     username = str(c), 
                     password = str(d), 
                     user_agent = "test")
reply = input("What do you want to reply with? ")
username = input("What user do you want to reply to?")
user = reddit.redditor(str(username))
myself = reddit.redditor(str(c))

for comment in user.comments.new():
    if myself.link_karma + myself.comment_karma > 1:
        try:
            a = random.randint(20,30)
            comment.reply(reply)
            sleep(a)
        except:
            continue
    else:
        try:
            comment.reply(reply)
            sleep(600)
        except:
            continue
