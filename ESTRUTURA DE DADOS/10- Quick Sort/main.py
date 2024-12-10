# Função para fazer a troca de elementos
def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

# Função de partição para o Quick Sort
def partition(lista, low, high, pivot_type='first'):
    # Escolha do pivô baseado no tipo especificado
    if pivot_type == 'first':
        pivot = lista[low]  # Pivô é o primeiro elemento
    elif pivot_type == 'last':
        pivot = lista[high]  # Pivô é o último elemento
    elif pivot_type == 'middle':
        mid = (low + high) // 2
        pivot = lista[mid]  # Pivô é o meio da lista

    # Colocar o pivô na posição correta (final da partição)
    i = low - 1
    for j in range(low, high):
        if lista[j] < pivot:
            i += 1
            swap(lista, i, j)
    
    # Colocar o pivô na posição correta
    swap(lista, i + 1, high if pivot_type != 'middle' else mid)
    return i + 1

# Função do Quick Sort
def quick_sort(lista, low, high, pivot_type='first'):
    if low < high:
        pi = partition(lista, low, high, pivot_type)
        quick_sort(lista, low, pi - 1, pivot_type)  # Recursão na partição esquerda
        quick_sort(lista, pi + 1, high, pivot_type)  # Recursão na partição direita

# Função para testar o Quick Sort
def testar_quick_sort():
    lista_quase_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_desordenada = [9, 7, 5, 3, 1, 10, 8, 6, 4, 2]

    print("Lista quase ordenada:", lista_quase_ordenada)
    quick_sort(lista_quase_ordenada, 0, len(lista_quase_ordenada) - 1, pivot_type='first')
    print("Lista ordenada (pivô primeiro):", lista_quase_ordenada)

    print("Lista desordenada:", lista_desordenada)
    quick_sort(lista_desordenada, 0, len(lista_desordenada) - 1, pivot_type='first')
    print("Lista ordenada (pivô primeiro):", lista_desordenada)

    # Testando com o pivô sendo o último elemento
    quick_sort(lista_quase_ordenada, 0, len(lista_quase_ordenada) - 1, pivot_type='last')
    print("Lista ordenada (pivô último):", lista_quase_ordenada)

    quick_sort(lista_desordenada, 0, len(lista_desordenada) - 1, pivot_type='last')
    print("Lista ordenada (pivô último):", lista_desordenada)

    # Testando com o pivô sendo o meio
    quick_sort(lista_quase_ordenada, 0, len(lista_quase_ordenada) - 1, pivot_type='middle')
    print("Lista ordenada (pivô meio):", lista_quase_ordenada)

    quick_sort(lista_desordenada, 0, len(lista_desordenada) - 1, pivot_type='middle')
    print("Lista ordenada (pivô meio):", lista_desordenada)

# Executar os testes
testar_quick_sort()
