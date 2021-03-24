"""
#Vamos aos exemplos:

#Exemplo 01: Pizzas

import matplotlib.pyplot as plt

#Gráfico de pizza. Cada fatia da pizza corresponde a um sabor diferente.

nome = 'Calabresa', 'Marguerita', '4 queijos', 'Shitake'
valores = [2, 2, 2, 2]
destaque = (0, 0, 0, 0)

plt.pie(valores, explode=destaque, labels=nome, autopct='%1.2f%%', startangle=90)
plt.legend(nome, title='Sabores', loc='right')
plt.axis("equal") #Permite que a caixa da legenda se movimente no gráfico conforme o tamanho da figura.
plt.title('Pizzas')
plt.show()


-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Vamos aos exemplos:

#Exemplo 02: Bolão Mega da Virada

import matplotlib.pyplot as plt

#Gráfico de pizza. Cada fatia corresponde a um valor de aposta na mega da virada. 

nome = 'Fellipe', 'Mariana', 'Paola', 'Bruna', 'Lucas', 'João'
valores = [220, 80, 75, 120, 95, 175]
destaque = (0, 0, 0, 0.1, 0.1, 0)

plt.pie(valores, explode=destaque, labels=nome, autopct='%1.2f%%', shadow=False, startangle=90)
plt.legend(nome, title='Apostadores', loc='best')
plt.axis("equal") #Permite que a caixa da legenda se movimente no gráfico conforme o tamanho da figura.
plt.title('Apostas Mega da Virada')
plt.show()

"""

#Vamos aos exemplos:

#Exemplo 03: Python avançado -> utilizando um dicionário para a criação de um gráfico. 

import matplotlib.pyplot as plt

#Gráfico de pizza. Cada fatia corresponde a um valor de aposta na mega da virada. 

grupo = {'Fellipe': 250, 'Paola': 275, 'Mariana': 175, 'Gina':120, 'Carlos': 90, 'Lucas':55}

nomes = tuple(grupo.keys())
valores = list(grupo.values())

destaque = (0, 0, 0, 0.1, 0.1, 0)

plt.pie(valores, explode=destaque, labels=nomes, autopct='%1.2f%%', shadow=False, startangle=90)
plt.legend(nomes, title='Apostadores', loc='best')
plt.axis("equal") #Permite que a caixa da legenda se movimente no gráfico conforme o tamanho da figura.
plt.title('Apostas Mega da Virada')
plt.show()




