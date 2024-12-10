import math
import time

# Pesquisa Binária adaptada para intervalos
def binary_search(sorted_list, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Pesquisa Exponencial
def exponential_search(sorted_list, target):
    # Verifica o primeiro elemento
    if sorted_list[0] == target:
        return 0

    # Salta exponencialmente até passar do alvo
    size = len(sorted_list)
    index = 1
    while index < size and sorted_list[index] < target:
        index *= 2

    # Realiza a busca binária no intervalo
    return binary_search(sorted_list, target, index // 2, min(index, size - 1))

# Teste da Pesquisa Exponencial
def test_exponential_search():
    sorted_list = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]
    target = 127

    # Chama o Exponential Search
    result = exponential_search(sorted_list, target)
    if result != -1:
        print(f"Elemento {target} encontrado na posição {result}.")
    else:
        print(f"Elemento {target} não encontrado.")

# Comparação de desempenho entre Exponential Search e Binary Search
def compare_exponential_binary_performance():
    list_sizes = [10**3, 10**4, 10**5, 10**6]
    target = 777

    for size in list_sizes:
        sorted_list = list(range(size))

        # Tempo do Exponential Search
        start_exp = time.time()
        exponential_search(sorted_list, target)
        exp_time = time.time() - start_exp

        # Tempo do Binary Search
        start_bin = time.time()
        binary_search(sorted_list, target, 0, len(sorted_list) - 1)
        bin_time = time.time() - start_bin

        print(f"Tamanho da lista: {size}")
        print(f"Tempo do Exponential Search: {exp_time:.6f} segundos")
        print(f"Tempo do Binary Search: {bin_time:.6f} segundos")
        print("-" * 40)

# Executa o teste de Exponential Search
test_exponential_search()

# Compara os desempenhos
compare_exponential_binary_performance()
