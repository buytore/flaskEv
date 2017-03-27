from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import thread
import time
import datetime
import sys

#host = '0.0.0.0'
host = ''
port = 8899
buf = 1024

addr = (host, port)

try:
    serversocket = socket(AF_INET, SOCK_STREAM)
    print 'TCP Socket created'
except socket.error, msg:
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

try:
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversocket.bind(addr)
    print'TCP Socket Bound'
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

serversocket.listen(10)


clients = [serversocket]

def handler(clientsocket, clientaddr):
    print "Accepted connection from: ", clientaddr
    while True:
        data = clientsocket.recv(1024)
        print "_" + data + "_"
        if data == "bye\n" or not data:
            clientsocket.send("Thanks for joining\n")
            break

        elif data.startswith("jpg_"): # jpg_/tmp/fotka.jpg
            file = data.split('_')[1].strip()
            try:
                bytes = open(file).read()
                print len(bytes)
                clientsocket.send(bytes)
            except IOError:
                print "File '" + file + "' not found!"
                clientsocket.send("FILE_NOT_FOUND\n")

        elif data == "test1\n":
            clientsocket.send("test1\n")

        elif "test2" in data: # Nemusi byt EOL, radeji nepouzivat!
            clientsocket.send("test2\n")

        else:
            clientsocket.send("ECHO: " + data.upper() + '\n')

    clients.remove(clientsocket)
    clientsocket.close()

def push():
    while True:
        for i in clients:
            if i is not serversocket: # neposilat sam sobe
                i.send("Curent date and time: " + str(datetime.datetime.now()) + '\n')
        time.sleep(10) # [s]


thread.start_new_thread(push, ())

while True:
    try:
        print "Server is listening for connections on Port: ", port
        clientsocket, clientaddr = serversocket.accept()
        clients.append(clientsocket)
        thread.start_new_thread(handler, (clientsocket, clientaddr))
    except KeyboardInterrupt: # Ctrl+C # FIXME: vraci "raise error(EBADF, 'Bad file descriptor')"
        print "Closing server socket..."
        serversocket.close()