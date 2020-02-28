'''
8. [net] Write a client-server application in which the client calls on the server to perform the operations in problem 7.
'''

# Server

import socket
import random
import string
import sys
from seven import *

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def menu_choice():
	ans = True

	while ans:
#		ans=input('What would you like to do? ') 
		if ans=='1':
#			while 1:
			ans = conn.recv(BUFFER_SIZE)
			print('Server received', ans)
			try:
				int_ans = int(ans)
				print(int_ans)
			except ValueError:
			   pass 	

			if not ans: 
				break

			answer = ''.join(int_ans)
			conn.send(answer)

			print(' [*] Factorial of an integer:') 
			print(' Factorial is {}'.format(integer_factorial()))

		elif ans=='2':
			print('[*] Prime number: ') 
		elif ans=='3':
			print('[*] Gcd: ') 
		elif ans=='4':
			print('[*] String to uppercase:')
		elif ans=='5':
			print('[*] Caesar encryption: ') 
		elif ans=='6':
			print('[*] Matrix * scalar: ') 
		elif ans=='7':
			print('\n Global symbols: ')
		elif ans=='8':
			print('\n [!] Goodbye!')
			sys.exit()
#		elif ans !='':
#			print('\n Not Valid Choice! Try again!') 

def main():
	print('Server: ')
	# connection
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((TCP_IP, TCP_PORT))
	server_socket.listen(1)

	print('Server listening...')
	conn, addr = server_socket.accept()
	print ('Connection address:', addr)

	menu_choice()

	conn.close()
if __name__ == '__main__':
	main()

