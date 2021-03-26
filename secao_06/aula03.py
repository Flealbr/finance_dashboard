"""
#Vamos aos exemplos

# Exemplo 01: Gráfico com duas barras

import matplotlib.pyplot as plt
import numpy as np

legenda =['Fellipe', 'Paola', 'Mariana', 'Luiz', 'Joana', 'Marina']
notas_p1 = [ 9.5, 8, 5, 7, 6, 4]
notas_p2 = [7.5, 9.5, 9, 8, 8, 9]

y = np.arange(len(legenda))
altura = 0.3

grafico01 = plt.barh(y - altura/2, notas_p1, height=altura, label='Notas P1', color='yellow')
grafico02 = plt.barh(y + altura/2, notas_p2, height=altura, label='Notas P2', color='Blue')

plt.xlabel('Notas')
plt.ylabel('Alunos')
plt.title("Notas do ano 2020")
plt.yticks(y, legenda)
plt.legend()

def legenda_automatica(grafico):
    #Adiciona legenda ao lado da barra
    for i in grafico:
        comprimento = i.get_width()
        plt.annotate(f'{comprimento}', xy=(comprimento, i.get_y() + i.get_height()/2),
        xytext=(10, 0), textcoords='offset points', ha='center')

legenda_automatica(grafico01)
legenda_automatica(grafico02)


plt.show()

"""

# Exemplo 02: Gráfico com três barras

import matplotlib.pyplot as plt
import numpy as np

legenda =['Fellipe', 'Paola', 'Mariana', 'Luiz', 'Joana', 'Marina']
notas_p1 = [ 9.5, 8, 5, 7, 6, 4]
notas_p2 = [7.5, 9.5, 9, 8, 8, 9]
notas_p3 = [9.5, 5.5, 8, 6, 5, 3]

y = np.arange(len(legenda))
altura = 0.3

grafico01 = plt.barh(y - 3*altura/2, notas_p1, height=altura, label='Notas P1', color='yellow', align='edge')
grafico02 = plt.barh(y, notas_p2, height=altura, label='Notas P2', color='Blue', align='center')
grafico03 = plt.barh(y + altura/2, notas_p3, height=altura, label='Notas P3', color='green', align='edge')

plt.xlabel('Notas')
plt.ylabel('Alunos')
plt.title("Notas do ano 2020")
plt.yticks(y, legenda)
plt.legend()

def legenda_automatica(grafico):
    #Adiciona legenda ao lado da barra
    for i in grafico:
        comprimento = i.get_width()
        plt.annotate(f'{comprimento}', xy=(comprimento, i.get_y() + i.get_height()/2),
        xytext=(10, 0), textcoords='offset points', ha='center')

legenda_automatica(grafico01)
legenda_automatica(grafico02)
legenda_automatica(grafico03)


plt.show()