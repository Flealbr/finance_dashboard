"""
import matplotlib.pyplot as plt

adicionaremos a linha:
plt.twin() esse comando já diz ao gráfico que usaremos o eixo x duas vezes para o plot de 2 gráfico diferentes.

# Exemplo:

import matplotlib.pyplot as plt 
import numpy as np 

# Criar nossos dados:

t = np.arange(0.01, 10, 0.01)
dados1 = np.exp(t)
dados2 = np.sin(2 * np.pi * t)

# Como já feito anteriormente:

plt.plot(t, dados1, color='red', label='exp(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('exp(t)', color='red')
plt.tick_params(axis='y', labelcolor='red') # Escrever o dados do eixo X em vermelho
plt.legend()


plt.twinx() # Linha FUNDAMENTAL para esse tipo de modificação. Comando que permite que o eixo X seja duplicado
plt.plot(t, dados2, color='blue', label='sen(2$\pi$t)')
plt.ylabel('sen(2$\pi$t)', color='blue')
plt.tick_params(axis='y', labelcolor='blue') # Escrever o dados do eixo X em Azul
plt.legend()

plt.title('Gráficos em função do tempo')
plt.show() 

"""

# Exemplo 02: Alterando a escalla

import matplotlib.pyplot as plt 
import numpy as np 

# Criar nossos dados:

t = np.arange(0.01, 10, 0.01)
dados1 = np.exp(t)
dados2 = np.sin(2 * np.pi * t)

# Como já feito anteriormente:

plt.plot(t, dados1, color='red', label='exp(t)')
plt.yscale('log')
plt.xlabel('Tempo (s)')
plt.ylabel('exp(t)', color='red')
plt.tick_params(axis='y', labelcolor='red') # Escrever o dados do eixo X em vermelho
plt.legend()


plt.twinx() # Linha FUNDAMENTAL para esse tipo de modificação. Comando que permite que o eixo X seja duplicado
plt.plot(t, dados2, color='blue', label='sen(2$\pi$t)')
plt.ylabel('sen(2$\pi$t)', color='blue')
plt.tick_params(axis='y', labelcolor='blue') # Escrever o dados do eixo X em Azul
plt.legend()

plt.title('Gráficos em função do tempo')
plt.show() 