# Gerar gráfico de dispersão utilizando temporary variable nos eixos do gráfico.
import numpy as np
import matplotlib.pyplot as plt


A = float(input("Insira o valor inicial = "))
B = float(input("Insira o valor final = "))
C = int(input("Insira a razão = "))
D = float(input("Insira o valor da potência de y = "))

x = np.arange(A,B,C)
y = np.arange(A,B,C)
plt.scatter(x,y**D)
plt.show()