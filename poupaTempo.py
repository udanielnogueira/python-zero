print('SISTEMA DO POUPA TEMPO')
print()

usuario = str(input('Digite seu nome: '))
print()

print('Bem vindo(a) ao sistema {}' .format(usuario))
print()

notas = float(input('Digite os valores de nota: '))
print()

cartao = float(input('Digite os valores de cartão: '))
print()

vale = float(input('Digite os valores de vale: '))
print()

moedaAtual = float(input('Digite os valores de moeda do dia atual: '))
print()

moedaAnterior = float(input('Digite os valores de moeda do dia anterior: '))
print()

moedaResultado = moedaAtual - moedaAnterior

caixa = notas + cartao + vale + moedaResultado

print('O VALOR DO CAIXA FOI {}' .format(caixa))
print()

print('Cálculo realizado')
print()