import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def main():
    print("Bem-vindo ao Programa de Comparação de Busca e Ordenação!")
    print("1. Ordenar uma lista")
    print("2. Procurar um elemento")
    escolha = input("Escolha uma opção (1 ou 2): ")

    if escolha == '1':
        array = list(map(int, input("Digite os números separados por espaços: ").split()))
        print("Algoritmos de ordenação disponíveis:")
        print("1. Bubble Sort")
        print("2. Quick Sort")
        escolha_ordenacao = input("Escolha um algoritmo de ordenação (1 ou 2): ")

        if escolha_ordenacao == '1':
            inicio_tempo = time.time()
            bubble_sort(array)
            tempo_decorrido = time.time() - inicio_tempo
            print(f"Lista ordenada (Bubble Sort): {array}")
        elif escolha_ordenacao == '2':
            inicio_tempo = time.time()
            array = quick_sort(array)
            tempo_decorrido = time.time() - inicio_tempo
            print(f"Lista ordenada (Quick Sort): {array}")
        else:
            print("Escolha inválida.")
            return

        print(f"Tempo gasto: {tempo_decorrido:.6f} segundos")

    elif escolha == '2':
        array = list(map(int, input("Digite uma lista ordenada de números separados por espaços: ").split()))
        alvo = int(input("Digite o número a ser procurado: "))
        print("Algoritmos de busca disponíveis:")
        print("1. Busca Linear")
        print("2. Busca Binária")
        escolha_busca = input("Escolha um algoritmo de busca (1 ou 2): ")

        if escolha_busca == '1':
            inicio_tempo = time.time()
            indice = linear_search(array, alvo)
            tempo_decorrido = time.time() - inicio_tempo
        elif escolha_busca == '2':
            inicio_tempo = time.time()
            indice = binary_search(array, alvo)
            tempo_decorrido = time.time() - inicio_tempo
        else:
            print("Escolha inválida.")
            return

        if indice != -1:
            print(f"Elemento encontrado no índice {indice}.")
        else:
            print("Elemento não encontrado.")
        print(f"Tempo gasto: {tempo_decorrido:.6f} segundos")

    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()