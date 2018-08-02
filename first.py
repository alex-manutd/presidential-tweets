#Analyze the President's tweets to determine if they are presidential
tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
tweet_words = tweet_string.split()
number_of_words = len(tweet_words)

number_of_good_words = 0
number_of_bad_words = 0

good_words = ["Thanks", "historic", "paychecks"]
bad_words = ["taxes"]

# Iterate through the words in the tweet tweet_string
for w in tweet_words:
        print(w)
        if w in good_words:
            number_of_good_words += 1
        elif w in bad_words:
            number_of_bad_words += 1

print ("There are " + str(number_of_good_words) + " good words in this tweet")
print ("There are " + str(number_of_bad_words) + " bad words in this tweet")

if number_of_good_words > number_of_bad_words:
    print ("What a presidential thing to say! HUGE!")
else:
    print ("Surely you are joking, Mr. Trump! SAD!")

#print (tweet_words)
#print ("Number of words in this tweet is: " + #str(number_of_words))

#Iterate through the words in the tweet tweet_string
#print ("Words in the tweet are:")
#for w in tweet_words:
#    len_of_w = len(w)
#    print("number of letters in " + w + " is " + #str(len_of_w) )
#print ("End of the words in the tweet")
