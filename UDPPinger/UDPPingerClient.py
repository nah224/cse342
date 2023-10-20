# UDPPingerClient.py
from socket import *
from time import *

# Store server address and port
serverAddress = ('localhost', 4041)
# Create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set client timeout at 1 second
clientSocket.settimeout(1.0)

# Iterate for 10 pings
for pingNumber in range(10):
    # Ping message to be sent
    msg = f'Ping {pingNumber}'.encode()
    # Store start time
    start = time()
    # Send message to server
    clientSocket.sendto(msg, serverAddress)

    # Attempt to get response message from server
    try:
        # Get response from server
        data, server = clientSocket.recvfrom(1024)
        # Store end time
        end = time()
        # Calculate round trip time
        rtt = end - start
        # Print response and rtt
        print(f'Response from {server[0]}: {data.decode()} - RTT: {rtt}')
    except timeout:
        # No response recieved
        print('Request timed out')

clientSocket.close()