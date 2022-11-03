from datetime import datetime

start = datetime.now()


def insertionSort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = open('/dados/dados5.txt').read().split(", ")

insertionSort(arr)
end = datetime.now()

arquivo = open('arquivosCriados/insertionSortPior100mil', 'x')
arquivo.write("Bruno Batista Ferreira\n")
arquivo.write("InsertionSort")
tempo = str(end - start)
arquivo.write("\n")
arquivo.write(tempo)
arquivo.write("\n")

for i in range(len(arr)):
    arquivo.write(arr[i] + ",")

