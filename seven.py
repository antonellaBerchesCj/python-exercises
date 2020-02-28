'''
7. [lang] Create functions which:
        a. Compute the factorial of an integer.
        b. Check if a number is prime.
        c. Compute the greatest common divisor of two numbers.
        d. Convert a string to uppercase.
        e. Caesar-encrypt (ROT3) a string.
        f. Multiply a matrix (given as a list of rows) by a scalar value. 
	e.g.: matrix of 3 rows, 2 columns: A = [[1, 2], [3, 4], [5, 6]] multiplied by 2 => [[2, 4], [6, 8], [10, 12]]
        g. Print the name and type of each global symbol with the following format:
            one entry per line
            name padded to the right to 10 with blanks, at most 10 characters
            colon (:)
            type (as returned by the type() function), truncated at 15 characters

        e.g.:

        a         :<type 'int'>
        __builtins:<type 'module'>
        __name__  :<type 'str'>
        __package_:<type 'NoneType
        [...]
'''

import re
import string
import numpy as np
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def integer_factorial():
	n = input('Enter an integer: ')
	n = int(n)
	fact = 1
	while n > 1:
	    fact = fact * n
	    n = n - 1
	return fact

def prime_number(n):
	if n == 0:
		return False
	elif n == 1:
		return False
	else:
		return all(n % i for i in range(2, n))
	# all(iterable) -> Returns True if all elements of the iterable are true (or if the iterable is empty)

def compute_gcd(a, b):
	if b == 0:
		return a
	else:
		return compute_gcd(b, a % b)

def uppercase_string():
	text = input('Insert a text: ')
	#text_no_numbers = ''.join([i for i in text if not i.isdigit()])
	#filtered_data = re.sub(r'[\W_]-', '', text)
	new_text = ""

	for litera in text:
		if litera.isalpha() == True:
			if litera.isupper() == False:
				litera = ord(litera) - 32
				new_text += chr(litera)
			else:
				new_text += litera
		else:
			new_text += litera
	return new_text

def Caesar_encrypt(plaintext):
	ciphertext = ''
	
	for letter in plaintext.lower():
		try:
			i = (alphabet.index(letter) + 3) % 26
			ciphertext += alphabet[i]
		except ValueError:
			ciphertext += letter

	return ciphertext.lower()
	
def matrix_x_scalar(scalar, matrix):
	for i in matrix:
		for j in i:
			result = scalar*np.array(matrix)
	return result

def create_random_value_matrix():
	random_matrix = np.random.random((2,3))
	return random_matrix


def main():
	print('Factorial is {}'.format(integer_factorial()))

#	print('Prime number: {}'.format(prime_number(int(n))))
#	
#	first = input('\nEnter first number: ')
#	second = input('Enter second number: ')
#	print('Greatest Common Divisor (of {} and {}) = {}'.format(int(first), int(second), compute_gcd(int(first), int(second))))
#	print(uppercase_string())
#	print ('Ciphertext: %s' % Caesar_encrypt(input('Enter the plaintext: ')))


#	matrix = np.array([[6,1,4],
#		     [9,2,5],
#		     [3,8,2]]) #use matrix or random_matrix
#	random_matrix = create_random_value_matrix()
#	print('Matrix:')	
#	print(random_matrix)
#	scalar = input('\nEnter a scalar: ')
#	print('Matrix multiplied by scalar {} is:'.format(scalar))
#	print(matrix_x_scalar(int(scalar), random_matrix))
	

if __name__ == "__main__":
	main()


