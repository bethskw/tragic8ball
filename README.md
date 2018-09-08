# Tragic 8 ball #
Twitter and/or Mastodon bot

Replies to yes/no questions with lines from tragic literature

# Bot behavior #

This bot reads its mentions, and looks for messages that contain a question
mark. Then it randomly chooses one of the lines from tragic_answers.txt for
its reply. 

The answers in that file are all lines from literary tragedies, such as
those of Shakespeare and Tolstoy. Feel free to add your own, or replace the
file with answers of your choice.

Literature used in creating the file: 

* King Lear

* Anna Karenina


# How to Tweet #

1. Create a Twitter account and app for your bot. 

2. Copy the API keys into tweet_secrets.py (an example file is included, but
you have to provide your own keys).

3. Set up a cron job that runs tweet_reply.py every minute.

# How to Toot #

1. Create a Mastodon account and app for your bot. 

2. Copy the access token into toot_secrets.py (an example file is included,
but you have to provide your own token).

3. Set up a cron job that runs toot_reply.py every minute.
