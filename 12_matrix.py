'''
12. [lang] Multiply a matrix of M rows & N columns by a matrix of N rows & M columns.
'''

def multiplication():
	# 3x3 matrix
	first_matrix = [[2,3,4],
		    [5,6,7],
		    [8,9,10]]
	# 3x4 matrix
	second_matrix = [[11,12,13,14],
		    [15,16,17,18],
		    [19,20,21,22]]

	# result is 3x4
	result_matrix = [[0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0]]

	# iterate through rows of X
	for i in range(len(first_matrix)):
		# iterate through columns of Y
		for j in range(len(second_matrix[0])):
			# iterate through rows of Y
			for k in range(len(second_matrix)):
				result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]

	print('First matrix:')
	for index in first_matrix:
		print(index)

	print('\nSecond matrix:')
	for index in second_matrix:
		print(index)

	print('\nResult matrix:')
	for index in result_matrix:
		print(index)

def main():
	multiplication()
	print()

if __name__ == '__main__':
	main()
