"""

# Vamos aos exemplos

import matplotlib.pyplot as plt

def funcao_terceiro_grau(x, a=1, b=1, c=1, d=1):
    Uma função que recebe cinco parâmetros de entrada, sendo que 4 últimos são opicionais com valores iguais a 1
    y = a * x ** 3 + b * x ** 2 + c * x + d
    return y

def funcao_segundo_grau(x, a=1, b=1, c=1):
    y = a * x ** 2 + b * x + c
    return y

lista_x = range(-5, 5)
lista_y_3 = []
lista_y_2 = []

for i in lista_x:
    lista_y_3.append(funcao_terceiro_grau(i))
    lista_y_2.append(funcao_segundo_grau(i, b=-3))

plt.plot(lista_x, lista_y_3, label='3 Grau', color='green')
plt.plot(lista_x, lista_y_2, label='2 Grau', color='purple')
#plt.scatter(lista_x, lista_y, color="green", marker='*')
plt.legend()
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Gráfico de f(x)')
plt.show()

"""


# Vamos aos exemplos

import matplotlib.pyplot as plt

def funcao_terceiro_grau(x, a=1, b=1, c=1, d=1):
    """ Uma função que recebe cinco parâmetros de entrada, sendo que 4 últimos são opicionais com valores iguais a 1"""
    y = a * x ** 3 + b * x ** 2 + c * x + d
    return y

def funcao_segundo_grau(x, a=1, b=1, c=1):
    y = a * x ** 2 + b * x + c
    return y


lista_x = range(-10, 10)
lista_map = list(map(funcao_segundo_grau, lista_x)) #utilizando a função map e transformando o resultado em uma lista

plt.plot(lista_x, lista_map, label='2 Grau', color='red')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Função Segundo Grau')
plt.legend()
plt.show()
