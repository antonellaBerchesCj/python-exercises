#! /usr/bin/env python
'''
21. [net] Given any show name (e.g. "The Simpsons") and a season / episode number, print the episode name and a brief description (use an online database, e.g. imdb.com or epguides.com).
'''

from urllib.request import urlopen
import sys
import requests
import sys
import re
import urllib.request
import os.path

def search_serial(html):
	title = '<h3 class="findSectionHeader"><a name="tt"></a>Titles</h3>'
	if title in html:
		search = html.split(title)[-1].split('</tr>')[0]
	
		idd = '/title/'
		if idd in search:
			id_serial = search.split(idd)[-1].split('/')[0]
		else:
			print('[!] Cannot find this serial')

	link = 'http://www.imdb.com/title/'	
	season = input('Season: ')
	id_serial = link + id_serial + '/episodes?season=' + season + '&ref_=tt_eps_sn_3'	
	html2 = requests.get(id_serial).text	

	episodes_list_page = '<div class="list detail eplist">'
	if episodes_list_page in html2:
		episodes_list = html2.split(episodes_list_page)[-1].split('<hr>')[0]
		#print(episodes_list)

		episode_input = input('Episode nr: ')
		episode_search = 'ttep_ep'+episode_input + '"'
		#print(episodes_list)
		if episode_search in episodes_list:
			ep_tag = episodes_list.split(episode_search)[-1].split('</strong>')[0]
			if 'title="' in ep_tag:
				ep = ep_tag.split('title="')[-1].split('"')[0]
				print('Episode name is: ' + ep)
	else:
		print('[!] Cannot find this episode')
			
			

def main():
	serial_name = input('Serial name: ')#'lie+to+me'
#	serial_name = serial_name.replace(' ','+')
	html = requests.get('http://www.imdb.com/find?q=' + serial_name + '&printable=yes').text
#	print(html)

	search_serial(html)

if __name__ == '__main__':
	main()
