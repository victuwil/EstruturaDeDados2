def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]

        # Recursão para dividir as listas
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Comparando as palavras para fundir as listas
        while i < len(left) and j < len(right):
            if left[i].lower() < right[j].lower():  # Ordem alfabética
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        # Adicionando os elementos restantes das listas
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

# Exemplo de uso
palavras = ["banana", "maçã", "laranja", "abacaxi"]
merge_sort(palavras)
print(palavras)
