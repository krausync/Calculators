import win32com.client as win32
from openpyxl.reader.excel import load_workbook, InvalidFileException
from openpyxl.workbook import Workbook
import pandas as pd
import xlrd

A = input("Insira aqui o Path = ")
B = input("Insira aqui o nome do arquivo = ")
C = input("Insira a extensão do arquivo = ")
caminho = A + "/" + B + "." + C
fname = caminho
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(fname)
# FileFormat = 56 is for .xls extension, FileFormat = 51 is for .xlsx extension
wb.SaveAs(fname+"x", FileFormat=51)  
wb.Close()  
excel.Application.Quit()
fname1 = pd.read_excel(caminho)
Agrupar = fname1.groupby("Categoria", as_index=False)["Valor"].sum()
print(Agrupar)
