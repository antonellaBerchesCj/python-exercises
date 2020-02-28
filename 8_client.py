'''
8. [net] Write a client-server application in which the client calls on the server to perform the operations in problem 7.
'''

# Client

import socket
import string

def connection():
	TCP_IP = '127.0.0.1'
	TCP_PORT = 5005
	BUFFER_SIZE = 1024

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((TCP_IP, TCP_PORT))

	print ('''
		1. Compute the factorial of an integer.
		2. Check if a number is prime.
		3. Compute the greatest common divisor of two numbers.
		4. Convert a string to uppercase.
		5. Caesar-encrypt (ROT3) a string.
		6. Multiply a matrix (given as a list of rows) by a scalar value. 
		7. Print the name and type of each global symbol
		8. Exit/Quit
		''')
	ans = input('What would you like to do? ') 
	client_socket.send(str(ans.encode('utf-8')))

	answer = client_socket.recv(BUFFER_SIZE)
	print(answer)

	client_socket.close()

def main():
	print('Client: ')
	connection()

if __name__ == "__main__":
	main()

