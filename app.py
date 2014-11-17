#!venv/bin/python

# all the imports
from flask import Flask, request, session, redirect, url_for, \
     abort, render_template, flash

import tweepy

# create application
app = Flask(__name__)

@app.route('/main', methods=['GET','POST'])
def main():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    tweet = request.form['tweet']
    print tweet
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)