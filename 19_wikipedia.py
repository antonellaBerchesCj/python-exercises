#!/usr/bin/python3
'''
19. [net] Retrieve the definition (and, if available, the main image) from the Wikipedia page of a given item.
'''

import requests
import sys
import re
import urllib.request
import os.path

def retrieve_image(html, word_to_search):
	a_clasa = "<html class"
	until_word = '</a>'

	if a_clasa in html:
		definition = html.split(a_clasa)[-1].split(until_word)[0]
	
		find2 = 'content='
		until2 = '/>'
		if find2 in definition:
			link_image = html.split(find2)[-1].split(until2)[0]
			link_image = link_image.replace('\"', "")
			extension = os.path.splitext(link_image)[1]

			try:
				data = urllib.request.urlretrieve(link_image, word_to_search + extension)
				print(link_image)
				print('\n[*] Image downloaded successfully!')
			except ValueError:
				print('\n[!] Cannot find any image!')
	

def clean_html(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def search_word_on_wikipedia(html, word_to_search):
	find = word_to_search
	word_to_search = word_to_search.title()
	search = '<b>' + word_to_search + '</b>'
	
	if '_' in search or '_' in find:
		search = search.replace('_', ' ')
		find = find.replace('_', ' ')
		word_to_search = word_to_search.replace('_', ' ')

	search2 = '<b>' + find + '</b>'
	until_word = '.'

	if search in html:
		definition = html.split(search)[-1].split(until_word)[0]
		definition = clean_html(definition)
		#print(word_to_search + definition)
	elif search2 in html:
		definition = html.split(search2)[-1].split(until_word)[0]
		definition = clean_html(definition)

	if len(definition) < 3000:
		print(word_to_search + definition)
	else:
		print('[!] Word cannot be found!')

def main():
	try:
		word_to_search = sys.argv[1]
	except Exception as e:
		print ("[!] Usage: python3 filename.py word_to_search")
		print('e.g. python3 19_wikipedia.py World_War_I')
		exit()

	html = requests.get('http://en.wikipedia.org/w/index.php?title=' + word_to_search+ '&printable=yes').text
	#print(html)

	search_word_on_wikipedia(html, word_to_search)
	retrieve_image(html, word_to_search)

if __name__ == '__main__':
	main()

