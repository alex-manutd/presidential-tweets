# Title: Surely you're joking Mr. Trump
# Author: Alex Zaslavsky (tutorial)
# Description: Analyze the President's tweets to determine if they are presidential

from nltk import word_tokenize
from nltk.stem.porter import *

stemmer = PortStemmer()

# Split a tweet string into words METHOD
def get_words(str):
    return str.split()

# Word weight Dictionary
word_weights = {"Thanks": 1.0, "historic": 0.5, "paychecks": 0.8, "taxes": -1.0}

# Calculate the average value of words in list_of_words METHOD
def get_average_word_weight(list_of_words):
    number_of_words = len(list_of_words)
    sum_of_word_weights = 0.0
    for w in list_of_words:
        if w in word_weights:
            sum_of_word_weights += word_weights[w]

    return sum_of_word_weights / number_of_words

tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"

words = get_words(tweet_string)
avg_tweet_weight = get_average_word_weight(words)

print ("The weight of the tweet is " + str(avg_tweet_weight))

if avg_tweet_weight > 0:
    print ("What a presidential thing to say! HUGE!")
else:
    print ("Surely you are joking, Mr. Trump! SAD!")

# Iterate through the words in the tweet tweet_string
# for w in tweet_words:
#         #print(w)
#        if w in good_words:
#            number_of_good_words += 1
#        elif w in bad_words:
#            number_of_bad_words += 1

#print ("There are " + str(number_of_good_words) + " #good words in this tweet")
#print ("There are " + str(number_of_bad_words) + " bad #words in this tweet")

#print (tweet_words)
#print ("Number of words in this tweet is: " + #str(number_of_words))

#Iterate through the words in the tweet tweet_string
#print ("Words in the tweet are:")
#for w in tweet_words:
#    len_of_w = len(w)
#    print("number of letters in " + w + " is " + #str(len_of_w) )
#print ("End of the words in the tweet")
