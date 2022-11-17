

def bubbleSort(array, movimentacoes, comparacoes):
    for final in range(len(array), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                comparacoes = comparacoes + 1
                array[current + 1], array[current] = array[current], array[current + 1]
                movimentacoes = movimentacoes + 1
                exchanging = True

        if not exchanging:
                return array, movimentacoes, comparacoes