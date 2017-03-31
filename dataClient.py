import socket
from random import randint
import time

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = '10.15.120.85'
port = 8899                # Reserve a port for your service.
print "The host is: " + host

s.connect((host, port))

print s.recv(1024)
s.close()