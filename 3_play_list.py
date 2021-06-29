'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira

Program: Playing with Lists
Based on: EIN420 Unity 3

'''
print()

lista=[]

'''

lista[0]='Daniel' e depois print(lista), daria erro
pois ainda não existe essa posição

'''
#metodo append, inlcui a posição e o valor
lista.append('Daniel') 
lista.append(2021)
lista.append('sistemas')
lista.append(1996)

print(lista)

#varrendo e imprimindo usando o enumerate
listax=[3,6,9,12,15,18,21]
for i,x in enumerate(listax, start=1):
	print(i,"=",x)


