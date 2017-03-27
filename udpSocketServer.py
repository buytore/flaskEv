'''
	Simple udp socket server
'''

import socket
import sys
from random import randint
import time

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8899  # Arbitrary non-privileged port

# Datagram (udp) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'udp Socket created'
except socket.error, msg:
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete on Port ', PORT

# now keep talking with the client
while 1:
    #d = s.recvfrom(1024)
    #data = d[0]
    #addr = d[1]

    localtime = time.asctime( time.localtime(time.time()))
    temperature = randint(-25, 45)
    pressure = randint(800, 1300)
    humidity = randint(0, 100)
    jsonString = str({'date': str(localtime), 'temp': temperature, 'press': pressure, 'humd': humidity})
    s.sendto(jsonString, addr)
    #print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + jsonString
    print jsonString

s.close()