import sys
import simplejson
import difflib
import os 
# Input argument is the filename of the JSON ascii file from the Twitter API
#filename = sample
 
tweets_text = [] # We will store the text of every tweet in this list
tweets_location = [] # Location of every tweet (free text field - not always accurate or given)
tweets_timezone = [] # Timezone name of every tweet
lengths = 0  #number of tweets that has text
#loop over all lines

os.chdir("411")
for files in os.listdir("."):
        if files.endswith(".txt"):
                print files

		f = file(files, "r")
		lines = f.readlines()
		for line in lines:
		        try:
		                tweet = simplejson.loads(line)

                # Ignore retweets!
#                if tweet.has_key("retweeted_status") or not tweet.has_key("text"):
#                        continue
		
				if not tweet.has_key("text"):
					continue

                # Fetch text from tweet
		                text = tweet["text"].lower()
		                places =  tweet["place"]
		                langa = tweet["user"]["lang"]
#		                print text + "/n"
#		if tweet["place"]:
#			coun = tweet["place"]["country_code"]
#			print coun	
#		print places
#		if places:
			# fetching country code
#			country = places["country_code"]

		# fetching language
#				langg = tweet["lang"]
                	# Ignore 'manual' retweets, i.e. messages starting with RT             
#                                if text.find("iphone") > -1:
#                                        lengths+=1
                                        #print text
                	        #continue
		                if langa == "en":
					if places:
						country = places["country_code"]
						if country == "US":
							with open("output/411.txt", "a") as text_file:
               							text_file.write("{}".format(line))
               							lengths+=1
#							print tweet
#							lengths+= 1					
#        	       	tweets_location.append( tweet['user']['location'] )
#        	       	tweets_timezone.append( tweet['user']['time_zone'] )
		        except ValueError:
				pass
       
 
# Show result
print lengths
#print len(tweet)
#print tweets_text
#print tweets_location
#print tweets_timezone
