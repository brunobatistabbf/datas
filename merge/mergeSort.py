def sort(array):
    aux = array[:]
    sort_half(array, aux, 0, len(array) - 1)


def sort_half(array, aux, start, end):
    if start >= end:
        return

    middle = (start + end) // 2

    sort_half(array, aux, start, middle)
    sort_half(array, aux, middle + 1, end)

    merge(array, aux, start, end)


def merge(array, aux, start, end):
    movimentacoes = 0
    comparacoes = 0
    left = start
    left_end = (start + end) // 2

    right = left_end + 1
    right_end = end

    for position in range(start, end + 1):
        if left > left_end:
            comparacoes += 1
            aux[position] = array[right]
            movimentacoes += 1
            right += 1

        elif right > right_end:
            comparacoes += 1
            aux[position] = array[left]
            movimentacoes += 1
            left += 1

        elif array[left] < array[right]:
            comparacoes += 1
            aux[position] = array[left]
            movimentacoes += 1
            left += 1

        else:
            comparacoes += 1
            aux[position] = array[right]
            movimentacoes += 1
            right += 1
    arquivoMovimentacoes = open('movimentacoes_comparacoes/movimentacoesMerge5.txt', "a")
    arquivoMovimentacoes.write(str(movimentacoes) + ", ")
    arquivoComparacoes = open('movimentacoes_comparacoes/comparacoesMerge5.txt', "a")
    arquivoComparacoes.write(str(comparacoes) + ", ")

    for k in range(start, end + 1):
        array[k] = aux[k]

    return array






