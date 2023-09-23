from socket import *

# Message to send
msg = "\r\n I love computer networks!"
endMsg = "\r\n.\r\n"

# Choose a mail server (e.g. mail.cse.lehigh.edu) and call it mailServer
mailServer = #Fill in start #Fill in end

# Create socket called clientSocket and establish a TCP connection with the mail server
#Fill in start
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
  print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
   print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
# Fill in start
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
# Fill in end

# Send DATA command and print server response.
# Fill in start
# Fill in end

# Send message data.
# Fill in start
# Fill in end

# Message ends with a single period.
# Fill in start
# Fill in end

# Send QUIT command and get server response.
# Fill in start
# Fill in end
