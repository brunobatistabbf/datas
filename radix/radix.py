from datetime import datetime

movimentacoes = 0
def countingSort(arr):
    movimentacoes = 0
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    count_arr = [0 for _ in range(range_of_elements)]

    output_arr = [0 for _ in range(len(arr))]


    for i in range(0, len(arr)):
        movimentacoes = movimentacoes + 1
        count_arr[arr[i] - min_element] += 1


    for i in range(1, len(count_arr)):
        movimentacoes = movimentacoes + 1
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        movimentacoes = movimentacoes + 1
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    for i in range(0, len(arr)):
        movimentacoes = movimentacoes + 1
        arr[i] = output_arr[i]

    return  movimentacoes
def radixSort(arr, movimentacoes):

	max1 = max(arr)

	exp = 1
	while max1 / exp >= 1:
		movimentacoes = countingSort(arr)
		exp *= 10




start = datetime.now()

def dados():
    arquivo = "dadosRadix/dados10_mil.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        dados = list(map(int, organizar))
    return dados

arr = dados()

radixSort(arr, movimentacoes)

end = datetime.now()

arquivo = open('arquvosCriados/dados10milRadix.txt', 'x')
arquivo.write("Bruno Batista Ferreira\n")
arquivo.write("Radix Sort")
tempo = str(end - start)
arquivo.write("\n")
arquivo.write(tempo)
arquivo.write("\n")

for i in range(len(arr)):
    arquivo.write(str(arr[i]) + ", ")
