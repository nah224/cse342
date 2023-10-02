# import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
serverSocket.bind(('', 4041))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        # Read and close file
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        httpHeader = 'HTTP:/1.1 200 OK\r\n'
        connectionSocket.send(httpHeader.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        fileNotFoundMsg = 'HTTP/1.1 404 Not Found\r\n'
        connectionSocket.send(fileNotFoundMsg.encode())
        fileNotFoundBody = '<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'
        connectionSocket.send(fileNotFoundBody.encode())
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
