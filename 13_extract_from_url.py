'''
[re] Extract all user agents from an Apache log file (e.g. http://redlug.com/logs/access.log); count the number of appearances for each distinct version of each user agent. e.g. from this:

"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"

the actual user agent is Chrome version 41.0.2272.101, but for the sake of simplicity we can assume that the first thing that looks like a user agent + version may be used ("Mozilla 5.0" in this case).
'''

import re
from collections import defaultdict

def parser():
	counter = defaultdict(int)
	with open('access.log') as f:
		for line in f:
			pattern = re.compile(r'(?P<agent>.*)')
			line = line.split('\" ', 1)[1].split('\"', 1)[1].split('\"', 1)[1].split('\"', 1)[1]	
			user_agent = line.partition('\" \"-\"')[0]

			m = pattern.match(user_agent)
			result = m.groupdict()
			
			for key, value in result.items():
				#print('User agent: %s ' % value)	
				counter[value] += 1
	
	for key, value in counter.items():
		print(key, ' - appearances:' , value)		
							
	return value

def main():
	parser()
	
if __name__ == '__main__':
	main()

