numeros = [12, 7, 14, 9, 3]
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[-1]
        menores = [x for x in lista[:-1] if x <= pivo]
        maiores = [x for x in lista[:-1] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

print("Antes:", numeros)
print("Depois:", quick_sort(numeros))
