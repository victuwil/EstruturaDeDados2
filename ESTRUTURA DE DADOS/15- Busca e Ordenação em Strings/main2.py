def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    left = []
    right = []

    for palavra in lista[1:]:
        if palavra.lower() < pivot.lower():  # Ordem alfabética
            left.append(palavra)
        else:
            right.append(palavra)

    return quick_sort(left) + [pivot] + quick_sort(right)

# Exemplo de uso
palavras = ["banana", "maçã", "laranja", "abacaxi"]
ordenadas = quick_sort(palavras)
print(ordenadas)
