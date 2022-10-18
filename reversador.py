
arr = open('dados/100milreverso.txt').read().split(" ")


arquivo = open('dados/insertionSort100milinverso.txt', 'x')


for i in range(len(arr)):
    arquivo.write(arr[i] + ",")