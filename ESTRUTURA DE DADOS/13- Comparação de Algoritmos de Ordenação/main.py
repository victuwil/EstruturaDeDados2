import random
import time

# Contadores globais de comparações
comparisons_shell = 0
comparisons_merge = 0
comparisons_selection = 0
comparisons_quick = 0
comparisons_bucket = 0
comparisons_radix = 0

# Função para Shell Sort
def shell_sort(lista):
    global comparisons_shell
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
                comparisons_shell += 1
            lista[j] = temp
        gap //= 2

# Função para Merge Sort
def merge_sort(lista):
    global comparisons_merge
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            comparisons_merge += 1
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

# Função para Selection Sort
def selection_sort(lista):
    global comparisons_selection
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons_selection += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Função para Quick Sort
def quick_sort(lista):
    global comparisons_quick
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    left = []
    right = []
    for x in lista[1:]:
        comparisons_quick += 1
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)

# Função para Bucket Sort
def bucket_sort(lista):
    global comparisons_bucket
    n = len(lista)
    if n == 0:
        return lista
    min_val, max_val = min(lista), max(lista)
    bucket_range = (max_val - min_val) / n
    buckets = [[] for _ in range(n)]
    for num in lista:
        index = int((num - min_val) // bucket_range)
        if index == n:
            index -= 1
        buckets[index].append(num)
    for i in range(n):
        buckets[i] = sorted(buckets[i])
        comparisons_bucket += len(buckets[i]) * (len(buckets[i]) - 1) // 2  # Contagem de comparações dentro de cada balde
    return [item for sublist in buckets for item in sublist]

# Função para Radix Sort
def radix_sort(lista):
    global comparisons_radix
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(lista, exp)
        exp *= 10

def counting_sort_radix(lista, exp):
    global comparisons_radix
    n = len(lista)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = lista[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = lista[i] // exp
        output[count[index % 10] - 1] = lista[i]
        count[index % 10] -= 1
    for i in range(n):
        lista[i] = output[i]
    comparisons_radix += n  # Contagem de comparações

# Função para testar e comparar os algoritmos
def testar_algoritmos():
    tamanhos = [10, 100, 1000, 5000]
    resultados = []
    
    for tamanho in tamanhos:
        lista = random.sample(range(1, 1000000), tamanho)  # Lista aleatória

        # Resetando os contadores de comparações
        global comparisons_shell, comparisons_merge, comparisons_selection, comparisons_quick, comparisons_bucket, comparisons_radix
        comparisons_shell = comparisons_merge = comparisons_selection = comparisons_quick = comparisons_bucket = comparisons_radix = 0

        # Testando Shell Sort
        lista_shell = lista.copy()
        start_time = time.time()
        shell_sort(lista_shell)
        shell_sort_time = time.time() - start_time

        # Testando Merge Sort
        lista_merge = lista.copy()
        start_time = time.time()
        merge_sort(lista_merge)
        merge_sort_time = time.time() - start_time

        # Testando Selection Sort
        lista_selection = lista.copy()
        start_time = time.time()
        selection_sort(lista_selection)
        selection_sort_time = time.time() - start_time

        # Testando Quick Sort
        lista_quick = lista.copy()
        start_time = time.time()
        lista_quick = quick_sort(lista_quick)
        quick_sort_time = time.time() - start_time

        # Testando Bucket Sort
        lista_bucket = lista.copy()
        start_time = time.time()
        lista_bucket = bucket_sort(lista_bucket)
        bucket_sort_time = time.time() - start_time

        # Testando Radix Sort
        lista_radix = lista.copy()
        start_time = time.time()
        radix_sort(lista_radix)
        radix_sort_time = time.time() - start_time

        # Armazenando resultados
        resultados.append({
            "Tamanho": tamanho,
            "Shell Sort (s)": shell_sort_time,
            "Merge Sort (s)": merge_sort_time,
            "Selection Sort (s)": selection_sort_time,
            "Quick Sort (s)": quick_sort_time,
            "Bucket Sort (s)": bucket_sort_time,
            "Radix Sort (s)": radix_sort_time,
            "Comparações Shell": comparisons_shell,
            "Comparações Merge": comparisons_merge,
            "Comparações Selection": comparisons_selection,
            "Comparações Quick": comparisons_quick,
            "Comparações Bucket": comparisons_bucket,
            "Comparações Radix": comparisons_radix
        })
    
    # Imprimir a tabela
    print(f"{'Tamanho':<10}{'Shell Sort (s)':<20}{'Merge Sort (s)':<20}{'Selection Sort (s)':<20}{'Quick Sort (s)':<20}{'Bucket Sort (s)':<20}{'Radix Sort (s)'}")
    print(f"{'Tamanho':<10}{'Comparações Shell':<20}{'Comparações Merge':<20}{'Comparações Selection':<20}{'Comparações Quick':<20}{'Comparações Bucket':<20}{'Comparações Radix'}")
    
    for resultado in resultados:
        print(f"{resultado['Tamanho']:<10}{resultado['Shell Sort (s)']:<20}{resultado['Merge Sort (s)']:<20}{resultado['Selection Sort (s)']:<20}{resultado['Quick Sort (s)']:<20}{resultado['Bucket Sort (s)']:<20}{resultado['Radix Sort (s)']}")
        print(f"{resultado['Tamanho']:<10}{resultado['Comparações Shell']:<20}{resultado['Comparações Merge']:<20}{resultado['Comparações Selection']:<20}{resultado['Comparações Quick']:<20}{resultado['Comparações Bucket']:<20}{resultado['Comparações Radix']}")

# Executar os testes
testar_algoritmos()
