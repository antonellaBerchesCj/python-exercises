'''
16. [web] Write a minimal web server which accepts POST file uploads from an HTML form and 
saves the uploaded files XOR-encoded into a local folder (module: bottle). 
Expose the list of encoded files & allow downloading the original, unencoded files.

Bonus points: include the file type (as returned by the file command) when listing stored files.
'''
from bottle import route, request, static_file, run, response
import os
import bottle
from itertools import cycle

directory = '/home/uploaded/'

@route('/')
def index():
	index_text = '''
	<head>
		<title>Web server</title>
	</head>
	<h2>Exercise 16</h2>
	<form action="/upload" method="POST" enctype="multipart/form-data">
		<p><input name="upload" id="file" type="file""></p>
	  	<p><input value="Start upload" type="submit"></p>
	</form>
	'''
	folder_str = "File successfully saved to '{0}'.".format(directory)

	list_files = []
	for filename in os.listdir(directory):
		#filename = xor(filename)
		list_files.append("<li><a href=\"" + filename + "\">" + filename + "</a></li>");
	return index_text  + '\n\n '.join(list_files)


@route('/upload', method='POST')
def do_upload():
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)
#	if ext not in ('.txt', '.doc', '.png', '.jpeg'):
#		return "File extension not allowed."

	if not os.path.exists(directory):
		os.makedirs(directory)

#	xored = [chr(ord(a) ^ ord(b)) for a,b in zip(bytes_from_file(fisier), cycle('secret'))]

	with open(upload.filename, 'rb+') as f:
		lines = f.read()
		lines_xored = [chr((a) ^ ord(b)) for a,b in zip(lines, cycle('secret'))]
		print(lines_xored)
		
		f_out = open(upload.filename, 'w') # in loc de upload.filename tb pus fisierul ce vine pus pe server
		f_out.write(str(lines_xored))
		f.close()
		f_out.close()

	with open(upload.filename, 'r') as f:
		lines = f.read()
		print('liness: ', lines)

	fisier = upload.filename
	
	file_path = "{path}/{file}".format(path=directory, file=fisier)
	upload.save(file_path)
	
	return bottle.redirect('/')

@route('/<filename>', method='GET')
def download_file(filename):
	f = open(directory + filename, 'rb')
	for line in f:
		content = f.read()
		#file_xored = [chr((a) ^ ord(b)) for a,b in zip(content, cycle('secret'))]
		f.close()
		response.set_header('Content-type', 'x-msdownload')

		return bytes(content)

def xor(data, key='secret'):
	#return bytearray(a^b for a, b in zip(*map(bytearray, [data, 'secret'])))
	return [chr(ord(a) ^ ord(b)) for a,b in zip(bytes_from_file(data), cycle(key))]

def bytes_from_file(filename):
	with open(directory + filename, 'rb') as f:
		lines = f.read()
		print(bytes(lines))
	return bytes(lines)

#	f = open(directory + filename, 'rb')
#	for line in f:
#		content = f.read()
#	f.close()

#	return bytes(content)

#def xor_encoding(filename):
#	byte = f.read(filename)
#	while byte != "":
#		xbyte = ord(byte) ^ k
#		g.write(chr(xbyte))
#		byte = f.read(filename)

if __name__ == '__main__':
	run(host='localhost', port=5000)

