'''
[lang] Find two coprime integers in the range 1e50..1e51.
1e50 = 1*10^50
'''
import collections

#m,n = map(int, input().split())
#for i in range(m, n+1):
#    #sqrt_num = int(n**(0.5))
#    sqrt_num = int(i**(0.5))
#    for j in range(2, sqrt_num+1):
#        if i%j == 0:
#            break
#    else:
#        print(i, end=', ')

#def gcd(a, b):
#	while b != 0:
#		a, b = b, a % b
#	return a


#def coprime(a, b):
#	return gcd(a, b) == 1

#def main():
#	a = int(1e50)
#	b = int(1e51)
#	print(b)
#	for i in range (a,b):
#		for j in range(a+1,b+1):
#			print(coprime(a,b))
#			a += 1
#			b += 1

def main():
	N = 15
	a = int(1e50)
	b = int(1e51)

	factors = [set() for n in range(N)]
	factored = collections.defaultdict(set)
	for n in range(2, N): #for n in range(2, N):
		if not factors[n]:           # no factors yet -> n is prime
			for m in range(n, N, n): # all multiples of n up to N
				factors[m].add(n)
				factored[n].add(m)

	for n in range(1, N):
		coprimes = set(range(1, N))  # start with all the numbers in the range
		for f in factors[n]:         # eliminate numbers that share a prime factor
			coprimes -= factored[f]
			print ("%d is coprime with %r others" % (n, len(coprimes)))

if __name__ == '__main__':
	main()
