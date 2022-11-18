from datetime import datetime
from quick import quicksort
from quicksort import quickSort
import sys
sys.getrecursionlimit()
sys.setrecursionlimit(5000)

movimentacoes = 0
comparacoes = 0

start = datetime.now()

def dados():
    arquivo = "dadosQuick/dados100milmelhor.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        dados = list(map(int, organizar))
    return dados

arr = dados()

array= quickSort(arr)

end = datetime.now()
tempo = str(end - start)

arquivo = open('arquivosQuick/dadosQuick100_milmelhor.txt', 'x')
arquivo.write("Bruno Batista Ferreira\n")
arquivo.write("Quick Sort")
arquivo.write("\n")
arquivo.write(tempo)
arquivo.write("\n")

for i in range(len(array)):
    arquivo.write(str(array[i]) + ", ")

arquivo.close()