
def sort(array, movimentacoes, comparacoes):
    comparacoes: int = 0;
    movimentacoes: int = 0;
    for index in range(0, len(array)):
           min_index = index


           for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                   comparacoes = comparacoes + 1
                   min_index =  right

            array[index], array[min_index] = array[min_index], array[index]
            movimentacoes = movimentacoes + 1

    return array, movimentacoes, comparacoes
