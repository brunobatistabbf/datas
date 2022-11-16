import random

def bogo_sort(arr,movimentacoes, comparacoes):
	comparacoes = 0
	movimentacoes = 0
	a = len(arr)
	comparacoes = comparacoes + 1
	while (sort(arr)== False):
		comparacoes = comparacoes + 1
		permutation(arr)
		movimentacoes = movimentacoes +  1
	if (sort(arr) == True):
		return arr, movimentacoes, comparacoes

def sort(array):
	a = len(array)
	for i in range(0, a-1):
		if (array[i] > array[i+1] ):
			return False
	return True

def permutation(array):
	a = len(array)
	for i in range (0,a):
		p = random.randint(0,a-1)
		array[i], array[p] = array[p], array[i]