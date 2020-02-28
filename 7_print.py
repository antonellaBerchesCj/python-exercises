
def printare():
	for k, v in globals().items():
#		print(k, ":", v)
		print('{:10.10}:{:15.15}'.format(str(k),str(type(v))))

def main():
	printare()

if __name__ == "__main__":
	main()


