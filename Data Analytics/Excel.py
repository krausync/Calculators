# Programa que irá solicitar o path, nome do arquivo e extensão e então fará a leitura do conteúdo da planilha.
import pandas as pd
A = input("Insira aqui o Path = ")
B = input("Insira aqui o nome do arquivo = ")
C = input("Insira a extensão do arquivo = ")
caminho = A + "/" + B + "." + C;
if C == "xlsx":
    teste = pd.read_excel(caminho)
    print(teste)
else: 
    teste2 = pd.read_csv(caminho)
    print(teste2)
