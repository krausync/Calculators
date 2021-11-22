# Esta calculadora irá calcular a velocidade média desenvolvida
# em uma determinada distância em função de um período de tempo.
a = float(input("Insira o valor da distância percorrida = "))
b = float(input("Insira o tempo em segundos = "))
c = int(input("Insira a quantidade de casas decimais = "))
velocidade = a/b;
print (round(velocidade, c), "m/s")