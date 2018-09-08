import random
import pawopy
from toot_secrets import *
from textgenrnn import textgenrnn

# neural netting
t=textgenrnn('/home/beth/tragic8ball/tragedies_weights.hdf5')

# for tooting
auth = pawopy.OAuthHandler( 'https://botsin.space' )
auth.set_access_token( A_TOKEN )
api = pawopy.API( auth )

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


# look through notifications
replies = api.notifications()
for reply in replies:
    # look for a question mark
    if reply.type == 'mention':
        if '?' in reply.status.content:
        #if reply.status.content.index('?') > 0:
            whatisay = get_answer()
            print("You asked: " + reply.status.content)
            print("And I might answer: " + get_answer())
            api.update_status_advanced({'status':'@' + reply.status.account.acct + " " + whatisay, 'in_reply_to_id':reply.status.id})

api.clear_notifications()

#### exploratory results
# replies = api.notifications()
# replies[0].type == "mention"
# replies[0].status.content # is the xml of the toot
# need to check content for a question mark
# if so, reply with: 
# api.update_status_advanced(
# in_reply_to_id = replies[0].status.id
# )
# api.clear_notifications()

 
#print("Okay, ready..." + get_answer() + "...done!") 



#toot = "The word of the hour is: " + thisword
#toot = thisword
#print(toot)

#api.update_status(toot) 
#print("...tooted!")
