'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira

Program: Playing with functions
Based on: EIN420 Unity 4

'''

def ola():
	print("Olá mundo!")

ola()

def exibe_nome(nome):
	print(nome)

print()

exibe_nome("Daniel")

print()

def cargo(nome, cargo): # cargo = "Analista", nome = "Daniel" passa independente da ordem
	print("O funcionário " + nome + " tem o cargo de " + cargo)

cargo("Daniel", "Analista")