numeros = [170, 45, 75, 90, 802, 24, 2, 66]

def counting_sort_por_digito(lista, exp):
    n = len(lista)
    saida = [0] * n
    contagem = [0] * 10  # dígitos 0-9

    for i in range(n):
        indice = (lista[i] // exp) % 10
        contagem[indice] += 1
  
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        saida[contagem[indice] - 1] = lista[i]
        contagem[indice] -= 1
        i -= 1

    for i in range(n):
        lista[i] = saida[i]

def radix_sort(lista):
    if not lista:
        return []
    
    max_valor = max(lista)

    exp = 1
    while max_valor // exp > 0:
        counting_sort_por_digito(lista, exp)
        exp *= 10

    return lista

print("Antes:", numeros)
print("Depois:", radix_sort(numeros))
