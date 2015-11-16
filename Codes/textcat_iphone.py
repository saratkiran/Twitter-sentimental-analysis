import sys
import simplejson
import difflib
import csv

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
				
					#print "new ##############"
					
				
			    with open('baby.csv', 'rb') as total:
				csvreader = csv.reader(total)
				for row in csvreader:
				    #print row[0]
				    if text.find(row[0]) > -1:
					with open("iphone_bytext.txt", "a") as text_file:    
						text_file.write("{}".format(line))
					break
				#    else:
				#	if hastagb:
				#		hashtag = [ hashtag['text'] for hashtag in hastagb ]
				#		for linners in hashtag:
				#			linnne = linners.lower()
				#			with open('baby.csv', 'rb') as total1:
				#				csvreader1 = csv.reader(total1)
				#				for row in csvreader1:
				#					if linnne.find(row[0]) > -1:
				#						with open("iphone_bytext.txt", "a") as text_file:    
				#							text_file.write("{}".format(line))
				#						break
									
			except:
			    pass

#with open('baby.csv', 'rb') as total:
#	 csvreader = csv.reader(total)
#	 for row in csvreader:
#	     print row[0]                 