"""
- Importando o módulo:
import matplotlib.pyplot as plt

- Criando o gráfico: pie 
plt.pie( vários parâmetros. Alguns obrigatórios, outros são necessários)
O único parâmetro obrigatório é um iterável contendo os valores de cada uma das partes da pizza.

Parâmetros necessários:
    - label (legendas): função que coloca uma legenda em cada uma das partes da pizza. Fun'ção recebe uma tupla
    - autopcp: Ao inserirmos o código '%1.2f%%'. Com este código será inserido no gráfico o valor percentual equivalente de cada fatia
    - explode: Uma função que permite destacar uma ou mais fatias da pizza. Recebe uma tupla com os valores.
    - shadow: função que coloca uma sombra no gráfico.
    - startangle: ângulo inicial que deseja começar a criar o gráfico. Tem como padrão 0 grau.

plt.legend(parametros adicionais):
é possível adicionar um título nessa caixa de legendas usando o comando "title=titulo";
é possível ajustar a localização da caixa com o comando "loc='posição'";
    - best;
    - upper right;
    - upper left
    - lower righ;
    - lower left
    - right;
    ....

plt.title(título do gráfico): mesmo comando do gráfico de dispersão
plt.show()

"""