'''
15. [lang] Create a generator function which returns the numbers from the Fibonacci sequence.
'''

import itertools as iterator

def fibonacci_generator(a=0, b=1):
    while 1:
        yield a
        b = a + b
        yield b
        a = a + b

max_iter = int(input('How many numbers? '))
for i in iterator.islice(fibonacci_generator(), max_iter):
    print(i, end = ', ')

print('...')
