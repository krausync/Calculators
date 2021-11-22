# Esta calculadora irá calcular o juros após t (tempo = meses).
# Fórmula base: m = c.(1+i)^t. 
# Inserir a taxa mensal como porcentagem real a.m.
# Inserir a taxa mensal separada por ponto e não vírgula, pois o código está como float.
a = float(input("Insira o capital inicial investido = "))
b = float(input("Insira a taxa contrata a.m = "))
c = float(input("Insira a quantidade de meses para investimento = "))
d = int(input("Insira a quantidade de casas decimais desejadas = "))
montante = a*((1+(b/100))**c);
juros = montante - a;
print("O Juros será de =", round(juros, d))
sair = (input("Digite 0 para encerrar ou 1 para refazer a conta = "))