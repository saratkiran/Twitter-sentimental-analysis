#!/usr/bin/env python
import time
import string
import simplejson
# read in liwc data file
def read_liwc(filename):
    liwc_data = open(filename, "r")
 
    mode = 0
    cat = {}
    dic = {}
 
    for line in liwc_data:
        line = line.strip("\r\n")
        if line == "%":
            mode += 1
            continue
 
        elif mode == 1:
            chunks = line.split("\t")
            cat[chunks[0]] = chunks[1]
 
        elif mode == 2:
            chunks = line.split("\t")
            word = chunks.pop(0)
            dic[word] = chunks
 
    return (cat,dic) # cat = list of categories, dic = list of all words with categories
 
# read in dictionary and partition it into set of positive and negative word
def get_wordsets(dic):
    posemo = {}
    negemo = {}
    for word in dic:
        for cat in dic[word]:
            if cat in ['126']:
                posemo[word] = dic[word]
                continue
        for cat in dic[word]:
            if cat in ['19', '127', '128', '129', '130']:
                negemo[word] = dic[word]
                continue
    return (posemo, negemo)
 
# determine if a tweet word matches an LIWC term (including prefix)
def matches(liwc_word, tweet_word):
    if liwc_word[-1] == "*":
        return tweet_word.startswith(liwc_word[:-1])
    else:
        return tweet_word == liwc_word
 
# general purpose function to determine if the string contains any of the
# substrings contained in set
def string_contains_any(string, set):
    for item in set:
        if item in string: return True
    return False
 
# returns the positivity/negativity score for the given tweet
def classify(tweet):
 
    pos_emoticons = [':-)', ':)', '(-:', '(:', 'B-)', ';-)', ';)']
    neg_emoticons = [':-(', ':(', ')-:', '):']
 
    # check for emoticons, if a consensus can be reached on sentiment
    # from emoticons, then just return that value
 
    emoticons_flag = 0
    if string_contains_any(tweet, pos_emoticons): emoticons_flag += 1
    if string_contains_any(tweet, neg_emoticons): emoticons_flag += 2
 
    if emoticons_flag == 1: return 1
    if emoticons_flag == 2: return -1
    if emoticons_flag == 3: return 0
 
    # if no emoticons:
 
    tweet = str(tweet.lower())
    words = tweet.split(" ")
 
    word_count = len(words)
    pos_count = 0.0
    neg_count = 0.0
 
    # classify each of the words
    for word in words:
        if len(word) == 0 or word[0] == '@': continue # if the word is prefixed with @, ignore it
        word = word.translate(string.maketrans("",""), string.punctuation) # strip punctuation
 
        # check if the words match posemo/negemo
        for pos in posemo:
            if matches(pos, word):
                pos_count += 1
        for neg in negemo:
            if matches(neg, word):
                neg_count += 1
 
    pos_score = pos_count/word_count
    neg_score = neg_count/word_count
 
    if pos_score > neg_score: return 1
    if pos_score < neg_score: return -1
    return 0
 
# --- CALLED ON IMPORT ---
 
cat, dic = read_liwc('liwc.dic')
posemo, negemo = get_wordsets(dic)
posleng = 0
neuleng = 0
negleng = 0
with open("out.txt", "a") as text_file:
    f = file("ushashtag5s.txt", "r")
    lines = f.readlines()
    for line in lines:
        try:
            tweet = simplejson.loads(line)
            if not tweet.has_key("text"):
                         continue
            text = tweet["text"].lower()
            tweet1 = text
            #print tweet1
            #tweet = "waiting for new  iphone :-)"
            output = classify(tweet1)
            
            num_output = int(output)
            if num_output == -1:
                negleng+=1
            elif num_output == 0:
                neuleng +=1
            else:
                posleng +=1

            
            
            text_file.write("{}".format(output1))
        except:
            pass
    
print "Positive tweets :" + str(posleng)
print "Negative tweets :" + str(negleng)
print "Neutral tweets :" + str(neuleng)
total =  posleng+negleng+neuleng
print "total tweets :" + str(total)

