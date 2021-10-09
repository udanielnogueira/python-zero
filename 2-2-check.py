'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira

Program: Checking Difference
Based on: EIN420 Unity 2

'''

import os
os.system('cls')

n1=float(input('Número 1: '))
n2=float(input('Número 2: '))


if n1==n2:
	print('Os números são iguais')
elif n1>n2:
	print('O número 1 é maior que o número 2')
else:
	print('O número 1 é menor que o número 2')

'''

uma versão mais simples seria apenas 
dizer se é igual ou diferente

'''