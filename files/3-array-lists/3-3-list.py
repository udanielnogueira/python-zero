'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira


Program: List of lists
Based on: EIN420 Unity 3

'''

listax = [[1, 2, 3, 4,], [5, 6, 7, 8]]
print(listax) # listas
print(listax[0]) # lista na posição 0

listax[0][1] = 1 # troca 2 por 1
print(listax[0])

listay = listax[0]

'''

lista y não recebe lista x[0]
ela é uma referência para ela
mudar lista x muda lista y
mudar lista y muda lista x

'''

listax[0][2] = 1 # troca 3 por 1
print("\nlista y referenciando x, lista y:", listay)