def selection_sort(lista):
    n = len(lista)
    
    # Percorre todos os elementos da lista
    for i in range(n):
        # Encontra o menor elemento na parte não ordenada
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        # Troca o elemento encontrado com o primeiro elemento não ordenado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        
        # Mostra o estado da lista após cada iteração
        print(f'Iteração {i+1}: {lista}')

# Exemplo de uso
lista = ["banana", "maçã", "laranja", "abacaxi", "morango"]
print("Lista inicial:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)
