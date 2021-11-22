# Esta calculadora irá calcular a área da seção circular.
# Fórmula base  = (𝜋∗(𝑑^2))/4
import math
a = float(input("Insira o valor do diâmetro [Metros]= "))
b = int(input("Insira a quantidade de casas decimais = "))
diametro = (math.pi*(a ** 2))/4;
print(round(diametro, b), "m²")
