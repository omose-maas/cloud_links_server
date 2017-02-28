#!/usr/bin/env python
# cording: utf-8
from socketIO_client import SocketIO, LoggingNamespace
import pyjsonrpc
import json
from cloud_links_core import BasicCommunication

ID = 1

class JsonRpc(pyjsonrpc.JsonRpc):
	def __init__(self, api_obj):
		api_methods = dir(api_obj)
		apis = filter(lambda m: not m.startswith('_'), api_methods)
		[self.__setitem__(api_obj.__class__.__name__ + "." + api ,getattr(api_obj,api)) for api in apis]

def on_my_resquest(request):
	response_json = rpc.call(request)
	
	socketIO.emit('my_response', response_json)


if __name__ == '__main__':
	driverlesscar = BasicCommunication()
	rpc = JsonRpc(driverlesscar)
	socketIO = SocketIO('localhost', 5000)
	socketIO.on('my_request', on_my_resquest)


	socketIO.wait()