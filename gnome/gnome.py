
def gnomeSort(arr, movimentacoes, comparacoes):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0:
            comparacoes = comparacoes + 1
            index = index + 1
        if arr[index] >= arr[index - 1]:
            comparacoes = comparacoes + 1
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            movimentacoes = movimentacoes + 1
            index = index - 1

    return arr , movimentacoes, comparacoes