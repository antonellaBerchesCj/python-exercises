'''
10. [lang] Print all primes between 100000000000 and 100000010000 (inclusive) separated by semicolons (;).
'''
lower = 100000000000
upper = 100000010000

from math import sqrt

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
# prime numbers are greater than 1
	if num > 1:
		for i in range(2,2+int(sqrt(num))):
			if (num % i) == 0:
				break
			else:
				print(num)
