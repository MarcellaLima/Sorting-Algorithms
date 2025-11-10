numeros = [5, 3, 8, 4, 2]

def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print("Antes:", numeros)
print("Depois:", bubble_sort(numeros))
