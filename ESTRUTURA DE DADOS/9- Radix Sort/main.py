import time

# Função de Counting Sort, usada para ordenar com base no dígito
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Lista para armazenar o resultado ordenado
    count = [0] * 10  # Contador para os dígitos de 0 a 9
    
    # Armazenar o número de ocorrências de cada dígito
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Alterar count[i] para que count[i] contenha a posição real dos dígitos
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir o array de saída
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    
    # Copiar o array ordenado para o array original
    for i in range(n):
        arr[i] = output[i]

# Função principal do Radix Sort
def radix_sort(arr):
    # Encontrar o maior número para saber o número máximo de dígitos
    max_num = max(arr)
    
    # Ordenar por cada dígito (começando da unidade, dezena, centena, ...)
    exp = 1  # Começando pelo dígito das unidades
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Função para testar o Radix Sort com números de diferentes tamanhos
def testar_radix_sort():
    tamanhos = [
        [23, 45, 67, 12, 89, 34],  # Lista com 2 dígitos
        [54321, 12345, 67890, 23456],  # Lista com 5 dígitos
        [9876543210, 1234567890, 4567891230, 9876543211]  # Lista com 10 dígitos
    ]
    
    for i, lista in enumerate(tamanhos):
        print(f"Testando lista com {len(str(lista[0]))} dígitos:")
        
        # Medindo o tempo do Radix Sort
        inicio = time.time()
        radix_sort(lista)
        tempo = time.time() - inicio
        
        print(f"Lista ordenada: {lista}")
        print(f"Tempo de execução: {tempo:.6f} segundos")
        print("-" * 40)

# Executa os testes
testar_radix_sort()
