from datetime import datetime
from merge import  mergeSort
from mergeSort import sort

movimentacoesValor = 0
comparacoesValor = 0

start = datetime.now()

def dados():
    arquivo = "dadosMerge/dados5.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        dados = list(map(int, organizar))
    return dados

movimentacoes = open('movimentacoes_comparacoes/movimentacoesMerge5.txt', "x")
comparacoes = open('movimentacoes_comparacoes/comparacoesMerge5.txt', "x")

array = dados()

sort(array)

def movimentacoes():
    movimentacoes =  "movimentacoes_comparacoes/movimentacoesMerge5.txt"
    with open(movimentacoes, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        listaMovimentacoes = list(map(int, organizar))

    return listaMovimentacoes

movimentacoesList = movimentacoes()

end = datetime.now()

arquivo = open('arquivosCriados/dados5merge.txt', 'x')
arquivo.write("Bruno Batista Ferreira\n")
arquivo.write("Combo Sort")
tempo = str(end - start)
arquivo.write("\n")
arquivo.write("Comparacoes: ")
comparacoesStr = str(comparacoesValor)
arquivo.write(comparacoesStr)
arquivo.write("\n")
movimentacoesStr = str(movimentacoesValor)
arquivo.write("Movimentacoes: ")
arquivo.write(movimentacoesStr)
arquivo.write("\n")
arquivo.write(tempo)
arquivo.write("\n")

for i in range(len(array)):
    arquivo.write(str(array[i]) + ", ")
