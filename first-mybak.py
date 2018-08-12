import json
import html
import twitter
import time

from nltk import word_tokenize, pos_tag
from nltk.stem.porter import *

# Split a tweet string into words METHOD
def get_words(str):
    useful_pos = {'NN'}
    tokens = word_tokenize(str)
    tags = pos_tag(tokens)
    return [word for word, pos in tags if pos in useful_pos]

# Load a jason object from a file
def load_json(json_file):
    with open(json_file) as f:
        return json.load(f)

# Calculate the average value of words in list_of_words METHOD
def get_average_word_weight(list_of_words, word_weights):
    number_of_words = len(list_of_words)
    sum_of_word_weights = 0.0
    print (number_of_words)
    if number_of_words == 0:
            return 0.0
    stemmer = PortStemmer()

# Interate through the words in the tweet string
    for w in list_of_words:
        stemmed_word = stemmer.stem(w)
        if stemmed_word in word_weights:
            sum_of_word_weights += word_weights[stemmed_word]

    return sum_of_word_weights / number_of_words

# Method to analyse the tweets using the word weight dictionary
def analyse_tweet(tweet_string, word_weights):
    words = get_words(tweet_string)
    avg_tweet_weight = get_average_word_weight(words, word_weights)
    print (tweet_string + ":" + str(avg_tweet_weight))

# Calls load_json() ie. dictionary
word_weights = load_json("word_weights.json")
credentials = load_json(".cred.json")

#Connect to the twitter API
twitter_api = twitter.Api(consumer_key=credentials["consumer_key"],
                          consumer_secret=credentials["consumer_secret"],
                          access_token_key=credentials["access_token_key"],
                          access_token_secret=credentials["access_token_secret"],
                          tweet_mode='extended')

# Load the last 10 status updates of Donald Trump
statuses = twitter_api.GetUserTimeline(screen_name="realDonaldTrump", count=10)

# Iterate through them and analyse them
for status in statuses:
    analyse_tweet(html.unescape(status.full_text), word_weights)
    prev_status = status.full_text

print (missing_words)
