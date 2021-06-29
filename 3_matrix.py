'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira

Program: Matrix
Based on: EIN420 Unity 3

'''

matrixA=[[5,7,8],[1,4,3],[9,5,2]]

for i in range(len(matrixA)):
	for j in range(len(matrixA[i])):
		print(matrixA[i][j]," ",end='')#end='' impede de pular linha
	print()


