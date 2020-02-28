'''
3.[re] Extract all ASCII strings of length >= 4 from a file (e.g. executable).
'''

import re
data = open('/home/notepad.exe','rb').read()

# Search for printable ASCII characters encoded as utf-8.
path = re.compile(ur'(?:[\x20-\x7E][\x00]){3,}')
words = [w.decode('utf-8') for w in path.findall(data)]
for w in words:
	if len(w) >= 4: 
	 	print(w)
