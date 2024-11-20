'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira

Program: Looping
Based on: EIN420 Unity 2

'''

#5 execuções
for i in range(5):
	print(i)
print('\n')

#i inicializa automaticamente com valor 0
for i in range(2):
	for k in range(3):
		print(i,k)
print('\n')

contador = 7
while contador <= 10:
	print('contador =', contador)
	contador += 1