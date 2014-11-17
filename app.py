#!venv/bin/python

# all the imports
from flask import Flask, request, url_for, render_template
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

import tweepy
from tstream import StdOutListener

# create application
app = Flask(__name__)

# consumer key and secrets
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET

# access token
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

# OAuth process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'GET':
	return render_template('index.html')
  else:
	search_term = request.form['tweet']
	search_term_hashtag = '#' + search_term
	
	listener = StdOutListener()
	
	stream = tweepy.Stream(auth, listener)
	print 'Stream started...'
	stream.filter(track=[search_term or search_term_hashtag])


if __name__ == '__main__':
	app.run(debug=True)