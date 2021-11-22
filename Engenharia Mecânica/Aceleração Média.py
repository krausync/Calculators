# Esta calculadora irá calcular a aceleração desenvolvida
# em uma determinada distância em função de um período de tempo.
a = float(input("Insira o valor da velocidade percorrida = "))
b = float(input("Insira o tempo em segundos = "))
c = int(input("Insira a quantidade de casas decimais = "))
aceleracao = a/b
print(round(aceleracao, c), "m/s²")
