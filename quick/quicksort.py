def quickSort(array, movimentacoes, comparacoes):
    fim = None
    inicio = 0
    if fim is None:
        fim = len(array) - 1

    if inicio < fim:
        p = partition(array, inicio, fim)
        quickSort(array, inicio, p-1)
        quickSort(array, p+1, fim)

    return array, movimentacoes, comparacoes

def partition(array, inicio, fim ):
    pivot = array[fim]
    i = inicio
    for j in range(inicio, fim):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i = i + 1
    array[i], array[fim] = array[fim], array[i]
    return  i
