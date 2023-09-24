from socket import *

# Message to send
msg = "\r\n I love computer networks!"
endMsg = "\r\n.\r\n"

# Choose a mail server (e.g. mail.cse.lehigh.edu) and call it mailServer
mailServer = 'mail.cse.lehigh.edu'

# Create socket called clientSocket and establish a TCP connection with the mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, 25))

recv = clientSocket.recv(1024).decode()
print(recv)
# Check for service ready code
if recv[:3] != '220':
  print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = f'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
   print('250 reply not received from server (recv1).')
 
# Send MAIL FROM command and print server response.
mailFrom = 'nah224@lehigh.edu'
mailFromCommand = f'MAIL FROM: {mailFrom}\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
   print('250 reply not recieved from server (recv2).')

# Send RCPT TO command and print server response.
rcptTo = 'nah224@lehigh.edu'
rcptToCommand = f'RCPT TO: {rcptTo}\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
   print('250 reply not recieved from server (recv3).')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
# Check for start mail input code
if recv4[:3] != '354':
   print('354 reply not recieved from server (recv4).')

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endMsg.encode())

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
# Check for service closing transmission channel code
if recv5[:3] != '221':
   print('221 reply not recieved from server (recv5).')
