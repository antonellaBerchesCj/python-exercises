'''
9. [encoding] Using the function randint(low, high) from the random module (find out what it does online), create a (global) dictionary mapping each lowercase letter of the alphabet to a unique 4-digit number (converted to string); print a multiline string encoded using this method. 

Bonus poins: create a function which decodes such an encoded string. Can you use the same dictionary?
'''

import random
import string

dictionary = {}
for i in string.ascii_lowercase:
	value = random.randint(1000, 9999)
	dictionary = {i:value}

def create_dic():
	dictionary = {}
	alphabet = string.ascii_lowercase	
	
	for i in alphabet:
		value = random.randint(1000, 9999)
		dictionary = {i:value}
	
	return dictionary

#	if value in dictionary.values():
#		print (value)


#	dictionary = random.randint(1000,9999)
	
#	while val in random_dict.values():
#		random_dict = random.randint(1000,9999)
#	print(random_dict[val])
#	return random_dict[val]


def create_random_dict(key):
	dictionar = {}
	for _ in range(26):
		n = random.randint(1000, 9999)
		if n not in dictionar:
			dictionar[key] = n
	return dictionar

def encoding():
#	values = dict()
#	for index, letter in enumerate(string.ascii_lowercase):
#		values[letter] = index + 1
#		print(values[letter])

#	values = {chr(i): i + 1 for i in range(ord("a"), ord("a") + 26)}
#	print(values)

	text = input('Enter a text to encode: ')

	if text.isalpha() == True or ' ' in text:
		for key in text:
			if ' ' not in key: 	# do not include space in mapping
				mydict = create_random_dict(key)
				for k,v in mydict.items():
					print(v, end = '')
	else:
		print('[!] Please enter only letters!')

def main():
	#print(create_dic())
	encoding()
	print()

if __name__ == "__main__":
	main()
