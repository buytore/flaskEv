'''
	Simple udp socket server
'''

import socket
import sys
from random import randint
import time

HOST = socket.gethostbyname()  # Symbolic name meaning all available interfaces
PORT = 8899  # Arbitrary non-privileged port
BUFF = 1024
# Datagram (udp) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'TCP Socket created'
except socket.error, msg:
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

# Bind socket to local host and port
s.bind((HOST, PORT))

print 'Socket bind complete on Port ', PORT

# now keep talking with the client
s.listen(5)
while 1:
    c, addr = s.accept()
    print 'Connected to ', addr
    localtime = time.asctime( time.localtime(time.time()))
    temperature = randint(-25, 45)
    pressure = randint(800, 1300)
    humidity = randint(0, 100)
    jsonString = str({'date': str(localtime), 'temp': temperature, 'press': pressure, 'humd': humidity})
    c.send(jsonString)
    print jsonString
    time.sleep(5)

s.close()