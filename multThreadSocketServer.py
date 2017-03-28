#!/usr/bin/env python
# from post: http://stackoverflow.com/questions/20745352/creating-a-multithreaded-server-using-socketserver-framework-in-python



import SocketServer
from threading import Thread


class service(SocketServer.BaseRequestHandler):
    def handle(self):
        data = 'dummy'
        print "Client connected with ", self.client_address
        while len(data):
            data = self.request.recv(1024)
            self.request.send(data)

        print "Client exited"
        self.request.close()


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


server = ThreadedTCPServer(('',8899), service)
server.serve_forever()