#!/usr/bin/env python
# cording: utf-8

#setup env
#pip install flask-socketio pyjsonrpc

from flask import Flask, render_template, session
from flask_socketio import SocketIO, send, emit, disconnect
import json
import pyjsonrpc
import send_socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	request_json = pyjsonrpc.create_request_json("BasicCommunication.get_status")
	send_socketio.send_data(socketio,request_json)
	return render_template('index.html')

@socketio.on('my_response')
def print_response_message(response):
	parsed_response = json.loads(response)
	print json.dumps(parsed_response, indent=4)


if __name__ == '__main__':
	socketio.run(app, port=5000)

