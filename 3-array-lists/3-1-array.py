'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira

Program: Arrays
Based on: EIN420 Unity 3

'''

lista1=['Daniel', 'Ane', 1, 2]
lista2=[7,8,9,10,11,12]

print('lista 1 [0]:', lista1[0])
print('lista 1 [3]:', lista1[3])

#negativo varre de trás para frente
print('\n')
print('lista 2 [-1]:', lista2[-1])

#1 inclusive, 2 exclusive
print('\n')
print('lista 2 [2:5]:', lista2[2:5])
print('lista 2 [-5:-2]:', lista2[-5:-2])

#varrendo e imprimindo a lista com +10
print('\n')
for x in lista2:
	print(x+10)

'''

[-2:-5] não funciona
leitura funciona da esquerda para a direita
do mais negativo para o menos negativo

'''