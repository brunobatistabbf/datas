def countSort(arr, movimentacoes, comparacoes):
    output = [0 for i in range(len(arr))]

    count = [0 for i in range(256)]
    movimentacoes = movimentacoes + 1

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1
        movimentacoes = movimentacoes + 1

    for i in range(256):
        count[i] += count[i - 1]
        movimentacoes = movimentacoes + 1
        comparacoes = comparacoes + 1

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        comparacoes =  comparacoes + 1
        count[ord(arr[i])] -= 1
        movimentacoes = movimentacoes + 1

    for i in range(len(arr)):
        ans[i] = output[i]
        movimentacoes = movimentacoes + 1
    return ans, movimentacoes, comparacoes