numeros = [64, 25, 12, 22, 11]

def selection_sort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

print("Antes:", numeros)
print("Depois:", selection_sort(numeros))
