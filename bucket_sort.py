numeros = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

def bucket_sort(lista):
    if not lista:
        return []

    n = len(lista)
    baldes = [[] for _ in range(n)]

    max_valor = max(lista)
    for num in lista:
        indice = int(num / (max_valor + 1) * n)
        baldes[indice].append(num)

    lista_ordenada = []
    for balde in baldes:
        lista_ordenada.extend(sorted(balde))  

    return lista_ordenada

print("Antes:", numeros)
print("Depois:", bucket_sort(numeros))
