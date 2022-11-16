from datetime import datetime
from bogo import bogoSort
from bogoSort import bogo_sort

movimentacoes = 0
comparacoes = 0

start = datetime.now()

arr = open('dadosBogo/dados5.txt').read().split(", ")

array, movimentacoes, comparacoes = bogo_sort(arr, movimentacoes, comparacoes)

end = datetime.now()

arquivo = open('arquivosCriados/dados5bogo.txt', 'x')
arquivo.write("Bruno Batista Ferreira\n")
arquivo.write("Bogo Sort")
tempo = str(end - start)
arquivo.write("\n")
arquivo.write("Comparacoes: ")
comparacoesStr = str(comparacoes)
arquivo.write(comparacoesStr)
arquivo.write("\n")
movimentacoesStr = str(movimentacoes)
arquivo.write("Movimentacoes: ")
arquivo.write(movimentacoesStr)
arquivo.write("\n")
arquivo.write(tempo)
arquivo.write("\n")

for i in range(len(array)):
    arquivo.write(array[i] + ", ")