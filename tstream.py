#!venv/bin/python

# all the imports
from flask import Flask

import tweepy
import simplejson as json

# listener that handles streaming data
class StdOutListener(tweepy.StreamListener):
	def on_connect(self):
		print 'Connection established...'

	# method called when raw data is received from connection
	def on_data(self, data):
		decoded = json.loads(data)
		# listen only for tweets that is geo-location enabled
		if decoded['geo']:
			tweet = {}
			tweet['screen_name'] = decoded['user']['screen_name']
			tweet['text'] = decoded['text'].encode('ascii', 'ignore')
			tweet['coord'] = decoded['geo']['coordinates']
			tweet['created_at'] = decoded['created_at']
			print tweet
			print ''
		return True

	def on_error(self, status):
		print status