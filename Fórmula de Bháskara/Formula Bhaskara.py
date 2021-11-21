#Este código irá calcular as raízes da equação no formato ax²+bx+c = 0
#Insira os valores de a, b e c
import math
a = float(input("Insira o valor de a = "))
b = float(input("Insira o valor de b = "))
c = float(input("Insira o valor de c = "))

# Esta parte irá calcular o delta
# A fórmula base é: Δ = b2 – 4ac
delta = (b*b)-(4*a*c);

# Esta parte irá calcular as raízes da função
# A fórmula base é:(−𝑏 ± √∆)/(2.𝑎)
if delta >0:
    bhaskara1 = ((-b) + math.sqrt(delta))/(2*a);
    bhaskara2 = ((-b) - math.sqrt(delta))/(2*a);
    print("O valor de delta é =", delta)
    print("O valor do X1 é =", bhaskara1)
    print("O valor do X2 é =", bhaskara2)
else:
    print("Está função não possui raízes reais.")            
