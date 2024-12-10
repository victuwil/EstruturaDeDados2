import math
import time

# Algoritmo Jump Search
def jump_search(sorted_list, target):
    n = len(sorted_list)
    jump = int(math.sqrt(n))  # O tamanho ideal do salto é √N
    prev = 0

    # Fase de saltos para encontrar o bloco correto
    while prev < n and sorted_list[min(jump, n) - 1] < target:
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Busca linear no bloco identificado
    for i in range(prev, min(jump, n)):
        if sorted_list[i] == target:
            return i

    return -1  # Retorna -1 se o elemento não for encontrado

# Algoritmo Binary Search
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Teste de desempenho e comparação
def test_algorithms():
    list_sizes = [1000, 10000, 100000, 1000000]  # Listas de tamanhos crescentes
    target = 777  # Elemento a ser encontrado

    for size in list_sizes:
        sorted_list = list(range(size))  # Lista ordenada

        # Medindo o tempo do Jump Search
        start_jump = time.time()
        jump_search(sorted_list, target)
        jump_time = time.time() - start_jump

        # Medindo o tempo do Binary Search
        start_binary = time.time()
        binary_search(sorted_list, target)
        binary_time = time.time() - start_binary

        print(f"Tamanho da lista: {size}")
        print(f"Jump Search: {jump_time:.6f} segundos")
        print(f"Binary Search: {binary_time:.6f} segundos")
        print("-" * 40)

# Chamando os testes
test_algorithms()
