#!venv/bin/python

# all the imports
from flask import Flask, request
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

import tweepy, redis
import simplejson as json

red = redis.StrictRedis()


# listener that handles streaming data
class StdOutListener(tweepy.StreamListener):
	
	def on_connect(self):
		print 'Stream starting...'

	# method called when raw data is received from connection
	def on_data(self, data):
		decoded = json.loads(data)
		# listen only for tweets that is geo-location enabled
		if decoded['geo']:
			tweet = {}
			tweet['screen_name'] = '@'+decoded['user']['screen_name']
			tweet['text'] = decoded['text'].encode('ascii', 'ignore')
			tweet['coord'] = decoded['geo']['coordinates']
			tweet['created_at'] = decoded['created_at']
			print 'A tweet received'
			# publish to 'tweet_stream' channel
			red.publish('tweet_stream', json.dumps(tweet))
			return True
		else:
			pass

	def on_error(self, status):
		print status

