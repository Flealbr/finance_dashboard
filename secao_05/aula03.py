"""
# Vamos os Exemplos

#Exemplo 01: 

import matplotlib.pyplot as plt
import numpy as np

legenda =['Fellipe', 'Paola', 'Mariana', 'Luiz', 'Joana', 'Marina']
notas_p1 = [ 9.5, 8, 5, 7, 6, 4]

x = np.arange(len(legenda)) #localizaçnao das legendas no eixo X
largura = 0.3 #Determina a largura das colunas


plt.bar(x, notas_p1, width=largura, label="Notas P1", color='blue')
plt.ylabel("Notas")
plt.title("Notas do primeiro trimestre")
plt.xticks(x, legenda)
plt.legend()
plt.show()

# Vamos os Exemplos

#Exemplo 02: gráfico com duas colunas 

import matplotlib.pyplot as plt
import numpy as np

legenda =['Fellipe', 'Paola', 'Mariana', 'Luiz', 'Joana', 'Marina']
notas_p1 = [ 9.5, 8, 5, 7, 6, 4]
notas_p2 = [7.5, 9.5, 9, 8, 8, 9]

x = np.arange(len(legenda)) #localizaçnao das legendas no eixo X
largura = 0.3 #Determina a largura das colunas


plt.bar(x - largura/2, notas_p1, width=largura, label="Notas P1", color='blue')
plt.bar(x + largura/2, notas_p2, width=largura, label='Notas P2', color='green')
plt.ylabel("Notas")
plt.title("Notas do primeiro trimestre")
plt.xticks(x, legenda)
plt.legend()
plt.show()

"""

# Vamos os Exemplos

#Exemplo 03: gráfico com duas colunas e valor da barra

import matplotlib.pyplot as plt
import numpy as np

legenda =['Fellipe', 'Paola', 'Mariana', 'Luiz', 'Joana', 'Marina']
notas_p1 = [ 9.5, 8, 5, 7, 6, 4]
notas_p2 = [7.5, 9.5, 9, 8, 8, 9]

x = np.arange(len(legenda)) #localizaçnao das legendas no eixo X
largura = 0.3 #Determina a largura das colunas


grafico_1 = plt.bar(x - largura/2, notas_p1, width=largura, label="Notas P1", color='blue')
grafico_2 = plt.bar(x + largura/2, notas_p2, width=largura, label='Notas P2', color='green')
plt.ylabel("Notas")
plt.title("Notas do primeiro trimestre")
plt.xticks(x, legenda)
plt.legend()

def legenda_automatica(grafico):
    #Adiciona a legenda em cima da barra do gráfico
    for i in grafico:
        altura = i.get_height()
        plt.annotate(f'{altura}', xy=(i.get_x() + i.get_width()/2, altura), xytext=(0, 2), textcoords='offset points', ha='center')



legenda_automatica(grafico_1)
legenda_automatica(grafico_2)
plt.show()