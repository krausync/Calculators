# Esta calculadora irá calcular o enésimo termo dentro de uma PA.
# Fórmula base: an = a1 + (n-1).r

a = float(input("Insira o valor de A1 = "))
b = float(input("Insira o valor de n = "))
c = float(input("Insira o valor de r = "))
d = float(input("Insira a quantidade de casas decimais = "))
termo = a + ((b-1)*c);
print(round(termo, d))