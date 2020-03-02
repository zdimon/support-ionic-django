#!/usr/bin/env python
import sys
import os
os.environ ['DJANGO_SETTINGS_MODULE'] = 'support.settings'
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.websocket import WebSocketHandler
# django settings must be called before importing models
from django.conf import settings
from support.settings import BROKER_URL
import tornadoredis
from django import forms
from django.db import models
from tornado import gen
from urllib.parse import urlparse
import json
import tornadoredis
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)
#subscriber = tornadoredis.pubsub.SockJSSubscriber(tornadoredis.Client())

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/tornado.html")


        
class EchoWebSocket(WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


class MessageHandler(tornado.websocket.WebSocketHandler):

    def __init__(self, *args, **kwargs):
        super(MessageHandler, self).__init__(*args, **kwargs)
        self.listen()

    @tornado.gen.engine
    def listen(self):
        self.client = tornadoredis.Client()
        self.client.connect()
        #yield tornado.gen.Task(self.client.subscribe, 'support-channel')
        self.client.subscribe('support-channel')
        self.client.listen(self.on_message)

    def on_message(self, msg):
        print(msg)
        try:
            msg = json.loads(msg.body)
            self.write_message(msg)
        except Exception as e:
            print(msg)
            print(str(e))
        #'due to a Redis server error.'
        #if msg.kind == 'message':
        #    self.write_message(str(msg.body))
        #if msg.kind == 'disconnect':
        # Do not try to reconnect, just send a message back
        # to the client and close the client connection
        #    self.write_message('The connection terminated '
        #                       'due to a Redis server error.')
        #    self.close()

    def check_origin(self, origin):
        return True

    def on_close(self):
        if self.client.subscribed:
            self.client.unsubscribe('support-channel')
            self.client.disconnect()

    def open(self, *args):
        print('Opennnnn')

class WebSocket(WebSocketHandler):
    def __init__(self, *args, **kwargs):
        self.client_id = None
        self._redis_client = None
        super().__init__(*args, **kwargs)

        #self._connect_to_redis()
        #self._listen()

    def redis_message_handler(message):
        print('Messageeeeee')
        print(message)

    def open(self, *args):
        print('Opennnnn')
        ps = redis_client.pubsub()
        ps.subscribe(**{'my-channel': self.redis_message_handler})

    def on_message(self, message):
        """
        :param message (str, not-parsed JSON): data from client (web browser)
        """
        print("on message")


    def on_close(self):
        print('on_close')




    
          
application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/echo", EchoWebSocket),
    (r"/socket", MessageHandler),
])

# Start the server
if __name__ == "__main__":
    print('Start tornado server')
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
