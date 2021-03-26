# Exemplo 03: Python avançado, utilizando dicionário e função zip()

import matplotlib.pyplot as plt 
import numpy as np 

alunos =['Fellipe', 'Paola', 'Mariana', 'Luiz', 'Joana', 'Marina']
notas_p1 = [ 9.5, 8, 5, 7, 6, 4]
notas_p2 = [7.5, 9.5, 9, 8, 8, 9]
notas_p3 = [9.5, 5.5, 8, 6, 5, 3]

dados_zip = zip(alunos, notas_p1, notas_p2, notas_p3)

#print(list(dados_zip))
# A partir desse zip(), vamos criar um dicionário em que a chave seja o anulo e o valor seja a maior nota.

y = np.arange(len(alunos))
altura = 0.3

dados_dic = {dados[0]: max(dados[1], dados[2], dados[3]) for dados in dados_zip}
print(dados_dic)

grafico01 = plt.barh(y, dados_dic.values(), height=altura, label='Maior nota', align='center', color='blue')

plt.xlabel('Notas')
plt.title("Pontuação por aluno")
plt.yticks(y, dados_dic.keys())
plt.legend()

def legenda_automatica(grafico):
    #Adiciona legenda ao lado da barra
    for i in grafico:
        comprimento = i.get_width()
        plt.annotate(f'{comprimento}', xy=(comprimento, i.get_y() + i.get_height()/2),
        xytext=(10, 0), textcoords='offset points', ha='center')

legenda_automatica(grafico01)

plt.show()