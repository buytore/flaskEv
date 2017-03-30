#!/usr/bin/env python
# from post: http://stackoverflow.com/questions/20745352/creating-a-multithreaded-server-using-socketserver-framework-in-python
import SocketServer
from SimpleWebSocketServer.SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

class SimpleEcho(WebSocket):

   def handleMessage(self):
      self.sendMessage(self.data)

   def handleConnected(self):
      pass

   def handleClose(self):
      pass

clients = []

class service(SocketServer.BaseRequestHandler):
    def handle(self):
        data = 'dummy'
        print "Client connected with ", self.client_address
        while len(data):
            data = self.request.recv(1024)
            if data:
                #self.request.send(data)
                server = SimpleWebSocketServer('localhost', 8000, "SimpleEcho")
                server.close()

        print "Client exited"
        self.request.close()


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


server = ThreadedTCPServer(('',8899), service)
server.serve_forever()