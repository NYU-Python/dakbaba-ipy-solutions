#!/usr/bin/env python

import flask
import requests

app = flask.Flask(__name__)
wsgi = app.wsgi_app


@app.route('/home')            #decorator indicates web URL
def home_page():
	return flask.render_template('index.html')

@app.route('/form.html')
def form():
	return flask.render_template('form.html')


@app.route('/stock_quote')
def stock_quote():
	stock = flask.request.args.get('stock')
	yahoo_url = "http://download.finance.yahoo.com/d/quotes.csv?s={0}&f=a".format(stock)
	stock_quote = requests.get(yahoo_url).content
	return flask.render_template("stock_quote.html", stock=stock, stock_quote=stock_quote)

'''
@app.route('/weather')
def weather():


@app.route('/headlines')
def headlines():
'''

if __name__ == '__main__':
    app.run(debug=True)    # app starts serving in debug mode
