"""
#Vamos aos exemplos:

# Exemplo 01:

import matplotlib.pyplot as plt
import numpy as np

N = 10000000 #Número de dados gerados
n_colunas = 50 #Número de colunas do histograma

x = np.random.randn(N)
plt.hist(x, bins=n_colunas, density=False, histtype='bar', color='purple', label='Histograma X')


N2 = 5000000
y = 10 + np.random.randn(N2)
plt.hist(y, bins=n_colunas, density=False, histtype='bar', color='green', label='Histograma Y')



plt.legend()
plt.title('Histograma')
plt.show()


"""
#Vamos aos exemplos:

# Exemplo 01:

import matplotlib.pyplot as plt
import numpy as np

N = 10000000 #Número de dados gerados
n_colunas = 25 #Número de colunas do histograma

x = np.random.randn(N, 4)

cores = [ 'blue', 'orange', 'purple', 'black']


plt.hist(x, bins=n_colunas, density=False, histtype='bar', color=cores, label=cores)


plt.legend()
plt.title('Histograma')
plt.show()

