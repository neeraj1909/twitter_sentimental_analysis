from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import json

def percentage(part, whole):
    return 100 * float(part)/ float(whole)


consumer_key= "57zMDJaEtD4gRluvVBHmjnPHE"
consumer_secret= "StXrbylpPHwHA8YqLXfo9DPl14srgxF2xCvR4bakzwpVWqCkTX"
access_token_key= "4864531754-JQ9NUln3BXUTU024a53uT7aKjrZA6cACmfU9KRz"
access_token_secret= "ODvIiSNsvqeq5HBJYFZL6D2rWuORjUh2C93JJgwN14Z1h"


auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
# api.update_status('tweepy + oauth!')

searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))


tweets =tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms)


positive = 0
negative = 0
neutral = 0
polarity = 0


for tweet in tweets:
    print(tweet.text)


