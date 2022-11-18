
def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    #porque só tem um elemento
    else:
        pivot = sequence.pop()

    #pop pega o ultimo elemento e o retorna
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


