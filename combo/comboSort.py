def combsort(array, movimentacoes, comparacoes):
    comparacoes = 0
    movimentacoes = 0
    gap = len(array)
    swaps = True

    while gap > 1 or swaps:
        comparacoes = comparacoes + 1
        gap = max(1, int(gap / 1.25))
        #gap minimo é um
        swaps = False
        for i in range(len(array) - gap):
            j = i+gap
            comparacoes = comparacoes + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                movimentacoes = movimentacoes + 1
                swaps = True

    return array, movimentacoes, comparacoes