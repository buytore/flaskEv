import sys, time
from socket import *

# Send UDP broadcast packets
HOST = ''
MYPORT = 8899

s = socket(AF_INET, SOCK_DGRAM)
print 'udp Socket created'
s.bind((HOST, MYPORT))
print "Bind"
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    data = repr(time.time()) + '\n'
    print "Set Time", data
    s.sendto(data, ('127.0.0.1', MYPORT))
    time.sleep(2)