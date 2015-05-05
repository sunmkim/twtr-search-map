# Geo-Locating Tweets in Real-Time


First off, I'd like to thank my friend [Mike Discenza](https://github.com/mdiscenza) and his [twitter_map](https://github.com/mdiscenza/twitter_map) project for the inspiration. In the initial stages of this project, I referred to his repo to get a better sense of how to utillize the [tweepy](https://github.com/tweepy/tweepy) library.

This application geo-locates, in real-time, tweets that contain a word or hashtag given
by the user. It only tracks tweets that allow the location feature, so it is not meant to be a comprehensive track of all tweets around the world.

Since learning Express for NodeJS, I've been really interested in making something with Flask,
and I thought this would be a fun and challenging project to take on, and it certainly was :)



## Technologies Used:
* Flask
* Redis
* Tweepy
* BackboneJS



## Real-Time Streaming
It was actually quite simple to initiate a filter-stream for tweets with the tweepy library.
The really difficult part of this project for me was figuring out how to push that data from the Flask server to the client in real-time. Python uses a WSGI-based server which is a synchronous protocol and can only handle one request at a time.

There are multiple ways to handle real-time data with Python and Flask, four of them being:
* AJAX
* Long Polling
* Web-sockets
* Server Sent Events (SSE)

### AJAX
Classic AJAX case. To use AJAX, I would have had to code an infinite loop on the client-side that would request the Flask server for tweets in intervals.

### Long Polling
The server would have to listen for the twitter-stream, wait for a tweet to come in, and then send a response
back to the client as soon as a tweet is received from the stream. The client would then have to immediately
send back another request to the server when that requested information is retrieved by the browser.

### Web-sockets
Having previously used socket.io, web-sockets was the first thing that came to my mind when I had to implement server-to-client data transfer. However, there weren't too many Flask extensions that would have accomplished my task in a straight-forward manner and/or had good documentation. Some extensions I found include [flask-sockets](https://github.com/kennethreitz/flask-sockets) and [flask-socketio](https://github.com/miguelgrinberg/Flask-SocketIO), but I felt that these were either not mature enough, lacked good documentation or was seemingly complex for my use.

### Server Sent Events
This was ultimately my choice for transferring real-time tweets from server to client. SSE is a newer communication protocol where the server will emit real-time events received by the browser. It's similar to web-sockets in that it happens in real time, but it's very much a one-way communication method from the server. To implement this, I first utilized Redis' Pub/Sub pattern to subscribe the server to the twitter-stream channel, and listen for incoming tweets in a handler where it would send those tweets to the client as a response. On the client-side, JavaScript code would listen for an event-source that would emit responses to the browser. As mentioned before, Python's WSGI does not support asynchronous programming. So, to make real-time data possible with Python, I used the Gevent library which patches Python standard library to enable asynchronous I/O and makes all code asynchronous without explicit context switching. And, behold! My browser can receive live data from Twitter!!



## Running This App
To run this app on your local machine, run these commands:
```
git clone https://github.com/kimasx/twtr-search-map.git
```
Then go into the repo directory and run
```
pip install flask redis tweepy simplejson gevent gunicorn
brew install redis
gunicorn --debug --worker-class=gevent -t 99999 app:app
```
Don't forget to have your redis-server running as well, and the app should be on `localhost:8000`.


## Future Considerations/Issues
- The major feature bug right now is that when you put in a new search, it doesn't stop the previous search. The server initiates a new search on top of the previous one. The Python server needs to be fixed so that it stops the previous stream listener.
	***Issue fixed. Big thanks to [mplorentz](https://github.com/mplorentz)!***
- A future feature that would be cool to implement is to have the app running for a certain amount of time given by the user and return a graph or chart of some sorts using d3.js.

