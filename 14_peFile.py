'''
14. [parsing] Print the number of sections of a PE executable whose filename is given as a parameter to the script (module: struct).
'''
import sys
import os
import struct

# Get WORD from byte array
def word(data, offset):
    return data[offset] + (data[offset+1]<<8)

# Get DWORD from byte array (file input)
def dword(data, offset):
	return struct.unpack('<I', data[offset:offset+4])[0]

def get_section_nr(file_name):
	with open(file_name, 'rb') as input:
		data = bytearray(input.read())

	if word(data, 0) != 0x5A4D: # MZ
		print(file_name + " - The file is not a MZ file")
		return False

	e_lfanew = dword(data, 60)
	ntHeader = e_lfanew
	nrSections = word(data, ntHeader+6)
	print('Nr. of sections: ', nrSections)


def main():
	if len(sys.argv) < 2:
		print("Please specify a file!")
		sys.exit()

	file_name = sys.argv[1]
	get_section_nr(file_name)

if __name__ == '__main__':
	main()
