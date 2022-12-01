def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr

def bucket_sort(arr):
    comparacoes = 0
    movimentacoes = 0
    aux_mov = 0
    result = []
    no_of_buckets = 5

    buckets = [[] for i in range(no_of_buckets)]

    max_elem, min_elem = max(arr), min(arr)
    bucket_size = (max_elem - min_elem) / no_of_buckets

    for element in arr:
        index = int((element - min_elem) / bucket_size)
        index -= 1 if element == max_elem else 0
        comparacoes = comparacoes + 1
        movimentacoes  = movimentacoes + 1
        buckets[index].append(element)
        movimentacoes  = movimentacoes + 1

    for bucket in buckets:
        result.extend(insertion_sort(bucket))
        movimentacoes = movimentacoes + 1

    return result, movimentacoes, comparacoes

