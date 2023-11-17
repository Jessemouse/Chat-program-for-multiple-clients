# Code skeleton provided by Ragnar Nohre
# Multi-client chat server using:
# Single-thread
# Listening on all clients simultaneously.
# Server wakes up on client connect and message sent. Starts listening again after.

#Server properties: 
# Single-threaded server uses "select" to handle multiple clients
# Several clients can connect at the same time
# A new client connection results in the message "[IP-address:portnr] (connected)" for all clients, except the new one.
#  When client sends msg to server, server sends msg to all other clients. Including sender in form "[IP:port] msg"
# A client disconnecting results in msg to all: "[IP:port] (disconnected)"

# ---- Imports ---- #
import socket
import select

# ---- Globals ---- #
port = 60_003
sock_l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ---- Program ---- #
sock_l.bind(("", port))
sock_l.listen(1)
list_of_sockets = [sock_l]
print("Listening on port {}".format(port))
while True:
    # Listens for inc data. 
    # Blocks program until any of the sockets in the list has inc. data or new client connection.
    tup = select.select(list_of_sockets, [], [])
    sock = tup[0][0]
    if sock==sock_l:
        pass
        # TODO: A new clients connects.
        # call (sockClient, addr) = sockL.accept() and take care of the new client
        # add the new socket to listOfSockets
        # notify all other clients about the new client
    else:
        # Connected clients send data or are disconnecting...
        data = sock.recv(2048)
    if not data:
        pass
        # TODO: A client disconnects
        # close the socket object and remove from listOfSockets
        # notify all other clients about the disconnected client
    else:
        pass
        # TODO: A client sends a message
        # data is a message from a client
        # send the data to all clients