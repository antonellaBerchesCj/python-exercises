'''
22. [os] Find duplicate files in a given folder + subfolders and automatically append the extension .dup (if not already present) to all but the first appearance (modules: os, hashlib).
'''
import os, sys
import hashlib
from os.path import join

def hash_file(path, blocksize = 65536):
	afile = open(path, 'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf) 
		buf = afile.read(blocksize)
	afile.close()
	return hasher.hexdigest()

def find_duplicates(parentFolder):
    # Dups in format {hash:[names]}
	dups = {}
	for dirName, subdirs, fileList in os.walk(parentFolder):
		print('Searching in %s...' % dirName)
		for filename in fileList:
			# Get the path to the file
			path = os.path.join(dirName, filename)
			# Calculate hash
			file_hash = hash_file(path)
			# Add or append the file path
			if file_hash in dups:
				dups[file_hash].append(path)
			else:
				dups[file_hash] = [path]
	return dups
 

def join_dicts(dict1, dict2):
	for key in dict2.keys():
		if key in dict1:
			dict1[key] = dict1[key] + dict2[key]
		else:
			dict1[key] = dict2[key]
 
def print_results(dict1):
	results = list(filter(lambda x: len(x) > 1, dict1.values()))
	if len(results) > 0:
		print('Duplicates Found: ')

		for result in results:
			for subresult in result:
				subresult = subresult.rsplit('/')
				old_file = subresult[-1]
				print('\t%s' % old_file)
				extension = os.path.splitext(old_file)[1]
				try:
					if '.dup' not in extension:
						new_file = old_file.replace(extension, extension + '.dup')
						os.rename(join(sys.argv[1], old_file), join(sys.argv[1], new_file))
				except: 
					pass
	else:
        	print('No duplicate files found.')

if __name__ == '__main__':
	if len(sys.argv) > 1:
		dups = {}
		folders = sys.argv[1:]
		for i in folders:
			# Iterate the folders given
			if os.path.exists(i):
				# Find the duplicated files and append them to the dups
				join_dicts(dups, find_duplicates(i))
			else:
				print('%s is not a valid path, please verify' % i)
				sys.exit()
		try:
			print_results(dups)
		except ValueError:
			pass
	else:
		print('Usage: python3 filename.py directory or python3 filename.py directory1 directory2 directory3')
