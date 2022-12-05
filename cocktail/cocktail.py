def cocktailSort(a, movimentacoes, comparacoes):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                comparacoes = comparacoes + 1
                a[i], a[i + 1] = a[i + 1], a[i]
                movimentacoes = movimentacoes + 1
                swapped = True
            else:
                comparacoes = comparacoes + 1

        if (swapped == False):
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                comparacoes = comparacoes + 1
                a[i], a[i + 1] = a[i + 1], a[i]
                movimentacoes = movimentacoes + 1
                swapped = True
            else:
                comparacoes = comparacoes + 1

        start = start + 1

    return a,movimentacoes, comparacoes,