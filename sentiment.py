import tweepy
from textblob import TextBlob

consumer_key = 'YOURS HERE'
consumer_secret = 'YOURS HERE'

access_token = 'YOURS HERE'
access_token_secret = 'YOURS HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Ripple')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
