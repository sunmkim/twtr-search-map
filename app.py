#!venv/bin/python

from flask import Flask, request, render_template, Response, stream_with_context, redirect, url_for, flash
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


import tweepy, redis
from tstream import StdOutListener

# consumer key and secrets
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET

# access token
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

# OAuth process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create application
app = Flask(__name__)
red = redis.StrictRedis()


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/search', methods=['POST'])
# gets search-keyword and starts stream
def streamTweets():
	search_term = request.form['tweet']
	search_term_hashtag = '#' + search_term
	# instantiate listener
	listener = StdOutListener()
	# stream object uses listener we instantiated above to listen for data
	stream = tweepy.Stream(auth, listener)
	stream.filter(track=[search_term or search_term_hashtag],
		async=True) # make sure stream is non-blocking
	redirect('/stream') # execute '/stream' sse
	return render_template('index.html')


@app.route('/stream')
def stream():
	# we will use Pub/Sub process to send real-time tweets to client
	def event_stream():
		# instantiate pubsub
		pubsub = red.pubsub()
		# subscribe to tweet_stream channel
		pubsub.subscribe('tweet_stream')
    # initiate server-sent events on messages pushed to channel
		for message in pubsub.listen():
			yield 'data: %s\n\n' % message['data']
	return Response(stream_with_context(event_stream()), mimetype="text/event-stream")


if __name__ == '__main__':
	app.run(debug = True, port=8000)

## run "gunicorn --debug --worker-class=gevent -t 99999 app:app --log-file=-" in terminal
## make sure to run "redis-server" in another tab in terminal
