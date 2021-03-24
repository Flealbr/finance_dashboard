"""
Fazendo os imports:
import matplotlib.pyplot as plt
import numpy as np

- Criando o Gráfico:
plt.bar(vários parâmetros): 2 parâmetros obrigatórios e alguns necessários.
Como parâmetro obrigatório:
    - o primeiro parâmetro obrigatório: um iterável com os valores no eixox a partir de onde as colunas crescerão.
    - O segundo parâmetro obrigatório: com os tamanhos (altura) das colunas.

Parâmetros adicionais: Necessários
    - width(largura): parâmetro que altera a largura das colunas. (recebe um valor numérico)
    - align(alinhamento) determina o alinhamento das colunas sobre o eixo x(recebe uma str:'center', 'edge')
    - label: escreve uma legenda no gráfico (recebe uma string)

plt.ylabel(str): Alterar a legenda do eixo y

plt.xticks(varios parametros) #Função Nova
    - o primeiro parametro obrigatorio: x(iterável) que determina onde os ticks aparecerão
    - o segundo parametro obrigatorio: legenda (iterável) coloca as legendas em cada ponto de X


plt.title(str): adiciona um título ao gráfico
plt.legend(parametro): coloca a legenda no gráfico
plt.show()

"""

