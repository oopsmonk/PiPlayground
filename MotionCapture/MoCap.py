#!/usr/bin/env python

from bottle import get, run, template, static_file
import os, inspect
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

rootPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

@get('/assets/<filepath:path>')
def assets_file(filepath):
    return static_file(filepath, root=rootPath+'/assets')

@get('/')
def index():
    return template('index')

@get('/websocket', apply=[websocket])
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else: break

run(host='127.0.0.1', port=8888, server=GeventWebSocketServer)

