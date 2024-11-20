'''

Programming Language: Python 3.9.4
Developer: Daniel Nogueira

Program: Área de um retângulo
Based on: EIN420 Unity 4

'''

def area_ret(p_base, p_altura):
	valor_area = p_base * p_altura
	return valor_area # não é procedimento de fato é função porque retorna

print("Cálculo de área do retângulo")
base = int(input("Base: "))
altura = int(input("Altura: "))

area = area_ret(base, altura)
print("Área: ", area)