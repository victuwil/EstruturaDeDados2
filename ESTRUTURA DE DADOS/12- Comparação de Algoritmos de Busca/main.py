import time
import math

# Função de Binary Search
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Função de Interpolation Search
def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Função de Jump Search
def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev, curr = 0, 0
    while curr < n and arr[curr] < x:
        prev = curr
        curr += step
    for i in range(prev, min(curr, n)):
        if arr[i] == x:
            return i
    return -1

# Função de Exponential Search
def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= x:
        i *= 2
    return binary_search(arr[i // 2:min(i, len(arr))], x)

# Função para comparar os tempos de execução
def comparar_tempos():
    tamanhos = [10**3, 10**4, 10**5, 10**6]  # Lista com diferentes tamanhos
    for tamanho in tamanhos:
        lista = list(range(tamanho))  # Lista ordenada

        # Escolhendo um valor a ser buscado (no meio da lista)
        x = tamanho // 2
        
        # Medindo o tempo do Binary Search
        inicio = time.time()
        binary_search(lista, x)
        tempo_binary = time.time() - inicio

        # Medindo o tempo do Interpolation Search
        inicio = time.time()
        interpolation_search(lista, x)
        tempo_interpolation = time.time() - inicio

        # Medindo o tempo do Jump Search
        inicio = time.time()
        jump_search(lista, x)
        tempo_jump = time.time() - inicio

        # Medindo o tempo do Exponential Search
        inicio = time.time()
        exponential_search(lista, x)
        tempo_exponential = time.time() - inicio

        print(f"Tamanho da lista: {tamanho}")
        print(f"Tempo do Binary Search: {tempo_binary:.6f} segundos")
        print(f"Tempo do Interpolation Search: {tempo_interpolation:.6f} segundos")
        print(f"Tempo do Jump Search: {tempo_jump:.6f} segundos")
        print(f"Tempo do Exponential Search: {tempo_exponential:.6f} segundos")
        print("-" * 40)

# Executar a comparação
comparar_tempos()
