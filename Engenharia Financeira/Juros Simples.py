# Esta calculadora irá calcular os juros simples após t (tempo = meses)
# Fórmula base - J = C.i.t
a = float(input("Insira o capital investido = "))
b = float(input("Insira a taxa contratada = "))
c = float(input("Insira o tempo contratado = "))
juros = a*(b/100)*c;
print(juros)
