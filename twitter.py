import tweepy
import os
from os import environ

consumer_key = 'moH0iauWm26FHz8WClJcHSM8G'
consumer_secret = 'bJ9c9vL4QtawLPaEeBDR1rtcvWjAhauFlz69AaY345gTGgrKlJ'
access_token = '1346148525608849413-XUFjMwwbiakYQbccZqJTTbS805KXQ6'
access_token_secret = 'CXIrrRh7ghDVckFaG8xwh1YDeqNhvJft4sayX8F1ehGV3'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

def generateTweet(tweet):
    api.update_status(tweet)
    print(tweet)
