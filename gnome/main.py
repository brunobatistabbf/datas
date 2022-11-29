from datetime import datetime
import gnome
from gnome import gnomeSort
movimentacoes = 0
comparacoes = 0

start = datetime.now()

def dados():
    arquivo = "dadosGnome/dados500_mil.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        dados = list(map(int, organizar))
    return dados

arr = dados()

array, movimentacoes, comparacoes = gnomeSort(arr, movimentacoes, comparacoes)

end = datetime.now()

arquivo = open('arquivosCriados/dados500MilGnome.txt', 'x')
arquivo.write("Bruno Batista Ferreira\n")
arquivo.write("Gnome Sort")
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
    arquivo.write(str(array[i]) + ", ")
