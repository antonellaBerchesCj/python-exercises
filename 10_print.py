'''
10. [lang] Print all primes between 100000000000 and 100000010000 (inclusive) separated by semicolons (;).
'''
from math import sqrt

lower = 100000000000
upper = 100000010000

print("Prime numbers between",lower,"and",upper,"are:")

#def is_prime(n):
#	if n <= 1:
#		return False
#	elif n <= 3:
#		return True
#	elif n % 2 == 0 or n % 3 == 0:
#		return False
#	i = 5
#	while i * i <= n:
#		if n % i == 0 or n % (i + 2) == 0:
#			return False
#	i = i + 6
#	return True


def main():
	dictionar = {}
	for num in range(lower,upper + 1):
		if num > 1:
			for i in range(2,2+int(sqrt(num))):
				i = num
				if (num % i) == 0:
					break
				else:
#					dictionar.update({i: num})
#					print(dictionar)
#					for k,v in dictionar.items():
#						print(v)
					if num not in i:
						print(i)
	
if __name__ == '__main__':
	main()



#for num in range(lower,upper + 1):
#	if num > 1:
#		for i in range(2,2+int(sqrt(num))):
#			if (num % i) == 0:
#				break
#			else:
#				print(num)
