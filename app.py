#!/usr/bin/env python
from __future__ import division

from flask import Flask, Response, redirect, request, url_for
import threading
import socket  # for sockets
import sys  # for exit
from random import randint, gauss
from time import sleep

app = Flask(__name__)

# Generate streaming data and calculate statistics from it
class MyStreamMonitor(object):
    def __init__(self):
        self.sum   = 0
        self.count = 0
        self.host = 'localhost'
        self.port = 8899

    @property
    def mu(self):
        try:
            # create dgram udp socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print 'Failed to create socket'
            sys.exit()

        while (1):
            msg = str(1)
            try:
                # Set the whole string
                s.sendto(msg, (self.host, self.port))
                # receive data from client (data, addr)
                d = s.recvfrom(1024)
                reply = d[0]
                addr = d[1]
                print reply
                # print 'Server 2 reply : ' + reply
                sleep(5)
            except socket.error, msg:
                print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                sys.exit()
        return d

stream = MyStreamMonitor()

@app.route('/')
def index():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            while True:
                yield "data: %s \n\n" % (stream.mu())
                sleep(.01) # artificial delay. would rather push whenever values are updated.
        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))

if __name__ == "__main__":
    # Data monitor should start as soon as the app is started.
    t = threading.Thread(target=stream.mu)
    t.start()
    print "Starting webapp..." # we never get to this point.
    app.run(host='localhost', port=23423)