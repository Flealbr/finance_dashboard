"""
Fazendo o import:
import matplotlib.pyplot as plt

import numpy as np

- Criando o gráfico:
plt.hist(varios parâmetros). O único parâmetro obrigatório é um iterável.
Alguns outros parâmetros que são úteis para uma boa formatação são:
    - bins: É um parâmetro que tem como objetivo determinar a quantidade de colunas do nosso histograma. Recebe um número inteiro
    - density: parâmetro booleano (True ou False). Se True, ao invës de colocar o número de ocorrências do evento, coloca a densidade que ocorre.
    - Color: alterar a cor do histograma
    - label: recebe uma string. Coloca uma legenda no histograma
    histype: Tem como padrão uma formato de barra, se alterada para 'barstacked' é desenhada apenas o contorno da barra do histograma.

plt.legend() -> aparecer as legendas do histograma
plt.title() -> aparecer o título do gráfico
plt.show()

"""