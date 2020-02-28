'''
18. [net] Write a script which takes as arguments an IP, a user and a password, connects to that IP as an FTP server and (recursively) copies all remote files to the current folder (module: ftplib).
'''
import os
import sys
import ftplib

def get_files_from_ftp(ip, user, passw, working_dir):
	path = '/share/images'

	ftp = ftplib.FTP(ip)
	ftp.login(user, passw)
	ftp.cwd(path)

	filenames = ftp.nlst() # get filenames within the directory
	file_list = []
	ftp.retrlines('LIST', lambda x: file_list.append(x.split()))

	for info in file_list:
		name = info[-1]
		ftp.retrbinary('RETR ' + name, open(name, 'wb').write)
	
	print('[*] Files have been copied successfully!')
	ftp.quit()

def remove_images_from_directory(working_dir):
	for item in os.listdir(working_dir):
		if item.endswith('.PNG'):
			os.remove(item)
	print('[*] Files have been deleted successfully!')

	
def main():
	if len(sys.argv) < 3:
		print('[!] Usage: python3 filename.py ip_address user password')
		sys.exit()

	working_dir = os.getcwd()

	ip_address = sys.argv[1]
	user = sys.argv[2]
	password = sys.argv[3]

	get_files_from_ftp(ip_address, user, password, working_dir)
	#remove_images_from_directory(working_dir)

if __name__ == '__main__':
	main()
