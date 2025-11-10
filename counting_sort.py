numeros = [4, 2, 2, 8, 3, 3, 1]

def counting_sort(lista):
    if not lista:
        return []
 
    max_valor = max(lista)

    contagem = [0] * (max_valor + 1)

    for num in lista:
        contagem[num] += 1

    lista_ordenada = []
    for i, quantidade in enumerate(contagem):
        lista_ordenada.extend([i] * quantidade)

    return lista_ordenada
  
print("Antes:", numeros)
print("Depois:", counting_sort(numeros))
