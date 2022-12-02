from datetime import datetime
import cocktail
from cocktail import cocktailSort

movimentacoes = 0
comparacoes = 0

start = datetime.now()

def dados():
    arquivo = "dadosCocktail/dados5.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        dados = list(map(int, organizar))
    return dados

arr = dados()

array, movimentacoes, comparacoes = cocktailSort(arr, movimentacoes, comparacoes)

end = datetime.now()

arquivo = open('arquivosCriados/dados5cocktail.txt', 'x')
arquivo.write("Bruno Batista Ferreira\n")
arquivo.write("Cocktail Sort")
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