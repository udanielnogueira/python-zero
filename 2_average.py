'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira

Program: Average Results
Based on: EIN420 Unity 2

'''

av1=float(input('Nota av1: '))
av2=float(input('Nota av2: '))

media=(av1+av2)/2
print('Média final:', media)

if media>=5:
	print('Aprovado')#identado, entao pertence ao if
	if media>=8:
		print('Parabéns pela grande nota')
else:
	print('Reprovado')
	print('Estude mais')