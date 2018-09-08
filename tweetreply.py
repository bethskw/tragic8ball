import random
import tweepy
from tweet_secrets import *


# for tweeting
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

def get_answer():
    # randomly choose yes or no
    #answers = ["Yes", "No,", "Yes", "No,", "Absolutely not", "Maybe ", "Reply hazy", "Signs point to", "Without a doubt", "Most likely", "Outlook not", "It is certain"]
    #myanswer = answers[random.randint(1,len(answers)-1)]
    # add a line from classic literature
    #myline = t.generate(1, return_as_list=True, prefix=myanswer, temperature=0.5)
    #return myline[0]
    return(get_line())

def get_line():
    # get random words
    word_file = "/home/beth/tragic8ball/tragic_answers.txt"
    words = open(word_file).read().splitlines()
    thisword = words[random.randint(1,len(words)-1)].capitalize()
    return thisword


### REPLACE CODE WITH WHATEVER i DID IN THE COCKTAILS BOT
mentions=api.mentions_timeline(count=200)
for mention in mentions:
    if mention.favorited:
        continue
    if '?' in mention.text:
        tweet = get_answer()
        print("You asked: " + mention.text)
        print("And I will answer: " + tweet)
        if len(tweet) > 256:
            tweet = tweet[0:255]
        tweetid = str(mention.id)
        tweet = '@' + mention.user.screen_name + ' ' + tweet
        api.update_status(tweet, in_reply_to_status_id=mention.id)
        mention.favorite() # fave to remember we've seen it
        print("Tweeted: " + tweet)