'''
	udp socket client
	Silver Moon
'''

import socket  # for sockets
import sys  # for exit
from random import randint
from time import sleep

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = '127.0.0.1';
port = 8899;

while (1):
    msg = str(randint(0,100))

    try:
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
        print reply
        #print 'Server 2 reply : ' + reply
        sleep(5)
    except socket.error, msg:
        print 'Error Code : '
        sys.exit()