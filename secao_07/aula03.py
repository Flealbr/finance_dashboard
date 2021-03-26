"""
Mudança no nosso código:

plt.annotate(varios parametros):
    - uma str com o texto que deseja anotar no gráfico;
    - xy = a posição x e y do texto. Com esse comando, é possível posicionar o local em que a str faz referência
    - xytext = posição no gráfico onde a str é escrita
    - arrowprops: recebe um dicionário tal que a chave desse dicionário é a cor da seta, e o valor é um valor numérico que diz o quanto a seta será encurtada.

# Exemplo
# plt.annotate('Valor Máximo', xy=(2, 1), xytext(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))

# Exemplo 01:

import matplotlib.pyplot as plt 
import numpy as np 

t = np.arange(0, 5, 0.01)
s = np.cos(2 * np.pi * t)

plt.plot(t, s, label='cos(2$\pi$', color='blue')
plt.annotate('Valor Máximo', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1))
plt.legend()
plt.title('Função Cosseno')
plt.ylim(-2, 2)
plt.show()

"""

import matplotlib.pyplot as plt 
import numpy as np 

t = np.arange(0, 5, 0.01)
y = 2 * t ** 2 - 3*t +1

y_minimo = min(y)
x_minimo = 0

for i in zip(t, y): #list(zip object) - [x, y]
    if i[1] == y_minimo:
        x_minimo = i[0]

plt.plot(t, y, label='cos(2$\pi$', color='blue')
plt.annotate('Ponto mínimo', 
            xy=(x_minimo, y_minimo), xytext=(x_minimo, y_minimo + 5), arrowprops=dict(facecolor='black', shrink=0.1))
plt.legend()
plt.title('Função 2 grau')
#plt.ylim(-2, 2)
plt.show()