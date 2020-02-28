'''
2. [net] Write a client / server pair of sources in which the client requests random numbers of a specific number of digits from the server.
'''
# Client
#!/usr/bin/env python
 
import socket
import string

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))

#client_socket.send('Send me random nr!')
digits = input("Enter nr of digits for random nr: ")
client_socket.send(str(digits))

randomNr = client_socket.recv(BUFFER_SIZE)
print(randomNr)

#digits = input("Enter nr of digits for random nr: ")
#if digits <= 10:
#	client_socket.send(string.digits)
#	randomNr = client_socket.recv(BUFFER_SIZE)
#	print(randomNr)
#else:
#	print('[!] Digit number must be <= 10!')

client_socket.close() 

