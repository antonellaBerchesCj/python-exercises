'''
2. [net] Write a client / server pair of sources in which the client requests random numbers of a specific number of digits from the server.
'''
# Server
#!/usr/bin/env python
 
import socket
import random
import string

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(1)

print('Server listening...')
conn, addr = server_socket.accept()
print ('Connection address:', addr)

while 1:
	digits = conn.recv(BUFFER_SIZE)
	print('Server received', digits)
	try:
		int_digits = int(digits)
	except ValueError:
		pass 	

	if not digits: 
		break

	random_nr = ''.join(random.sample('0123456789', int_digits))
	conn.send(random_nr)

conn.close()
