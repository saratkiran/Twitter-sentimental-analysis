import sys
import simplejson
import difflib

tweets_text = [] # We will store the text of every tweet in this list
tweets_location = [] # Location of every tweet (free text field - not always accurate or given)
tweets_timezone = [] # Timezone name of every tweet
lengths = 0  #number of tweets that has text

os.chdir("1")
for files in os.listdir("."):
        if files.endswith(".txt"):
                print files

		f = file(files, "r")
		lines = f.readlines()
#f = file("10.txt", "r")
#lines = f.readlines()
                for line in lines:
                        try:
                                tweet = simplejson.loads(line)
                                if not tweet.has_key("text"):
                                        continue
                                text = tweet["text"].lower()
                
                                entities = tweet["entities"]
                                if entities:
                                        hastagb = tweet["entities"]["hashtags"]
                                        if hastagb:
                 #                               hashtag = tweet["entities"]["hashtags"]['text']
                                
                              #  if entities:
                  #                  hashtagblock = entities["hashtags"]
                 #                   if hashtagblock:
                                                hashtag = [ hashtag['text'] for hashtag in hastagb ]
                                                #print hashtag
                                                #lineer = hashtag.readlines()
                                                with open("sampler.txt", "a") as text_file:
                                                        for linners in hashtag:
                                                                linnne = linners.lower()
                                                                if linnne.find("iphone") > -1:
                                           #     if hastagb:
                                           
                                                                        print linnne
                                                                        text_file.write("{}".format(line))
                                                                        lengths+=1
                                                                if linnne.find("apple") > -1:
                                           #     if hastagb:
                                                                        text_file.write("{}".format(line))
                                                                        print linnne
                                                                        lengths+=1
                                                       
                        except ValueError:
                                pass
print lengths
