# Esta calculadora irá calcular os juros simples após t (tempo = meses)
# Fórmula base - J = C.i.t
a = float(input("Insira o capital investido = "))
b = float(input("Insira a taxa contratada = "))
c = float(input("Insira o tempo contratado = "))
d = int(input("Insira a quantidade de casas decimais = "))
juros = a*(b/100)*c;
print(round(juros, d))
