import sys
import simplejson
import difflib

tweets_text = [] # We will store the text of every tweet in this list
tweets_location = [] # Location of every tweet (free text field - not always accurate or given)
tweets_timezone = [] # Timezone name of every tweet
lengths = 0  #number of tweets that has text

f = file("411.txt", "r")
lines = f.readlines()
for line in lines:
        try:
                tweet = simplejson.loads(line)
                if not tweet.has_key("text"):
                        continue
                text = tweet["text"].lower()
                if text.find("iphone") > -1:
                        lengths+=1
                        print text
        except ValueError:
                pass
print lengths
