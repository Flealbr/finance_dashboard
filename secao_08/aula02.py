"""
Vamos criar um dicionário que contenha como chave o número de alunos e como valor tenha um tupla com a nota das 6 provas feitas ao longo do semestre.

Nosso projeto consistirá em:
    - Criar um gráfico de pizza com a porcentagem de alunos aprovados e reprovados;
    - Criar um histograma com as médias finais dos alunos;
    - Criar um gráfico de colunas mostrando as 3 maiores notas de cada um. 

"""

import matplotlib.pyplot as plt 
import numpy as np 
import random

# Nossos Dados:

n_alunos = range(1, 26)

dados = {}

for posicao in n_alunos:
    chave = str(posicao)
    prova = 1
    notas = []
    while prova <= 6:
        nota = random.randrange(0, 11)
        notas.append(nota)
        prova += 1 
    
    dados.update({chave:notas})


# Calcule a média dos alunos: A média será formada pelas 3 maiors notas obtidas pelo aluno

def ordena_notas(listagem):
    ordenadas = sorted(listagem, reverse=True)
    return ordenadas

def calcula_media(listagem): # Função que calcula a média das 3 maiores notas
    lista_ordenada = ordena_notas(listagem)
    pos = 0
    soma = 0
    while pos < 3:
        soma += lista_ordenada[pos]
        pos += 1
    return round(soma/3, 2) # Função round arredenda os valores numéricos e o '2' é a quantidade de casas decimais. 

media_alunos = {chave: calcula_media(valor) for chave, valor in dados.items()}

print(media_alunos)





