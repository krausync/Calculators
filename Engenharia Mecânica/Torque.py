# Esta calculadora irá calcular o torque fornecido em um braço em função da força.
a = float(input("Insira o valor da força exercida [Newton] = "))
b = float(input("Insira o valor do raio [Metros] = "))
c = int(input("Insira a quantidade de casas decimais = "))
torque = a * b;
print(round(torque, c), "N.m")
