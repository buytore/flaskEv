import socket
from random import randint
import time

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = 'localhost'
port = 8898                # Reserve a port for your service.
print "The host is: " + host
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('<HTML><p>Thank you for connecting</p>')
   newNum = randint(0, 100)
   c.send("<p>Here's your random number" + str(newNum)+"</p>")
   c.close()                # Close the connection