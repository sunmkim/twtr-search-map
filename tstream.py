#!venv/bin/python

# all the imports
from flask import Flask

import tweepy
import simplejson as json


# listener that handles streaming data
class StdOutListener(tweepy.StreamListener):
	# method called when raw data is received from connection
	def on_data(self, data):
		decoded = json.loads(data)
		# listen only for tweets that is geo-location enabled
		if decoded['geo']:
			screen_name = decoded['user']['screen_name']
			tweet = decoded['text'].encode('ascii', 'ignore')
			coord = decoded['geo']['coordinates']
			print '@%s: %s %s' % (screen_name, tweet, coord)
			print ''
		return True

	def on_error(self, status):
		print status