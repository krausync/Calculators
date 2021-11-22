# Esta calculadora irá calcular o enésimo termo dentro de uma PA.
# Fórmula base: an = a1.(q^(n-1))

a = float(input("Insira o valor de A1 = "))
b = float(input("Insira o valor de n = "))
c = float(input("Insira o valor de q = "))
d = float(input("Insira a quantidade de casas decimais = "))
termo = a*(c ** (b-1))
print(round(termo, d))
