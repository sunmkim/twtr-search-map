#!venv/bin/python

# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# create application
app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)