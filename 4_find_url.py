# coding: utf-8
'''
4. [re] Find all URLs and / or email addresses in a text file.
'''

import re
import sys 

def find_urls(filename):	
	with open(filename) as f:
		content = f.readlines()
		str_content = ''.join(content)
#		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str_content)
		urlss = re.findall('(?:http://|www.)[^"\' ]+', str_content)		
		for u in urlss:
			print(u)

def find_emails(filename):
	with open(filename) as f:
		content = f.readlines()
		str_content = ''.join(content)
		emails = re.findall(r'[\w\.-]+@[\w\.-]+', str_content)
		for e in emails:
			print(e)

def main():
	if len(sys.argv) < 2:
		print("Please specify a file!")
	else:
		filename = sys.argv[1]
		print('URLs:')
		find_urls(filename)
		print('\nEmails:')
		find_emails(filename)

if __name__ == '__main__':
    main()
