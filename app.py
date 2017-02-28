#!/usr/bin/env python
# cording: utf-8

#setup env
#pip install flask-socketio pyjsonrpc

from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, send, emit, disconnect
import json
import pyjsonrpc
import send_socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
count = 0

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/post', methods = ['POST'])
def hello():
	if request.method == 'POST':
		if request.form['action'] == 'post':
			data = {'latitude' : request.form['latitude'], 'longitude' : request.form['longitude']}
			request_json = pyjsonrpc.create_request_json("DriverlessCar.set_destination",data)
			send_socketio.send_data(socketio,request_json)
		#test
		global count
		count = count + 1
	return render_template('index.html', message = count)

@socketio.on('my_response')
def print_response_message(response):
	parsed_response = json.loads(response)
	print json.dumps(parsed_response, indent=4)


if __name__ == '__main__':
	socketio.run(app, port=5000)

