# UDPPingerClient.py

# The client should send 10 pings to the server. Because UDP is an unreliable 
# protocol, a packet sent from the client to the server may be lost in the network,
# or vice versa. For this reason, the client cannot wait indefinitely for a reply
# to a ping message. You should get the client to wait up to one second for a reply;
# if no reply is received within one second, your client program should assume that
# the packet was lost during transmission across the network. You will need to look
# up the Python documentation to find out how to set the timeout value on a datagram socket.

# (1) send the ping message using UDP (Note: Unlike TCP, you do not need to establish a connection first, since UDP is a connectionless protocol.) 
# (2) print the response message from server, if any 
# (3) calculate and print the round trip time (RTT), in seconds, of each packet, if server responds 
# (4) otherwise, print “Request timed out” 

from socket import *

serverAddress = ('localhost', 4041)

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1.0)

for pingNumber in range(10):
    msg = f'Ping {pingNumber}'.encode()

    clientSocket.sendto(msg, serverAddress)

    try:
        data, server = clientSocket.recvfrom(1024)

        print(f'{data.decode()}')
    except timeout:
        # No response recieved
        print('Request timed out')

clientSocket.close()