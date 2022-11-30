def countingSort(arr):
    movimentacoes = 0
    comparacoes = 0
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    count_arr = [0 for _ in range(range_of_elements)]
    comparacoes = comparacoes + 1
    movimentacoes = movimentacoes + 1
    output_arr = [0 for _ in range(len(arr))]
    comparacoes = comparacoes + 1
    movimentacoes = movimentacoes + 1

    for i in range(0, len(arr)):
        comparacoes = comparacoes + 1
        count_arr[arr[i] - min_element] += 1
        movimentacoes = movimentacoes + 1

    for i in range(1, len(count_arr)):
        comparacoes = comparacoes + 1
        count_arr[i] += count_arr[i - 1]
        movimentacoes = movimentacoes + 1

    for i in range(len(arr) - 1, -1, -1):
        comparacoes = comparacoes + 1
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        movimentacoes = movimentacoes + 1
        count_arr[arr[i] - min_element] -= 1
        movimentacoes = movimentacoes + 1

    for i in range(0, len(arr)):
        comparacoes = comparacoes + 1
        arr[i] = output_arr[i]
        movimentacoes = movimentacoes + 1

    return arr, movimentacoes, comparacoes