from datetime import datetime
from combo import  comboSort
from comboSort import  combsort

movimentacoes = 0
comparacoes = 0

start = datetime.now()

def dados():
    arquivo = "dadosComb/dados500_mil.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        dados = list(map(int, organizar))
    return dados

arr = dados()

array, movimentacoes, comparacoes = combsort(arr, movimentacoes, comparacoes)

end = datetime.now()

arquivo = open('arquivosCriados/dados500milcombo.txt', 'x')
arquivo.write("Bruno Batista Ferreira\n")
arquivo.write("Combo Sort")
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
