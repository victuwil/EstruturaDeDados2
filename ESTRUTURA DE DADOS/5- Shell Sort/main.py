import time
import math

# Função de Shell Sort com a sequência de intervalo Shell
def shell_sort_shell(lista):
    n = len(lista)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = temp
        intervalo //= 2

# Função de Shell Sort com a sequência de intervalo Knuth
def shell_sort_knuth(lista):
    n = len(lista)
    intervalo = 1
    # Calcula o maior intervalo possível de acordo com a fórmula de Knuth
    while intervalo < n // 3:
        intervalo = intervalo * 3 + 1
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = temp
        intervalo //= 3

# Função de Shell Sort com a sequência de intervalo Hibbard
def shell_sort_hibbard(lista):
    n = len(lista)
    intervalo = 1
    # Calcula o maior intervalo possível de acordo com a fórmula de Hibbard
    while intervalo <= n // 2:
        intervalo = 2 * intervalo + 1
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = temp
        intervalo = (intervalo - 1) // 2

# Função para comparar os tempos de execução
def comparar_shell_sort():
    tamanhos = [10**3, 10**4, 10**5]  # Lista com diferentes tamanhos
    for tamanho in tamanhos:
        lista = [i for i in range(tamanho, 0, -1)]  # Lista invertida para pior caso

        # Medindo o tempo do Shell Sort com a sequência Shell
        inicio_shell = time.time()
        shell_sort_shell(lista.copy())
        tempo_shell = time.time() - inicio_shell

        # Medindo o tempo do Shell Sort com a sequência Knuth
        inicio_knuth = time.time()
        shell_sort_knuth(lista.copy())
        tempo_knuth = time.time() - inicio_knuth

        # Medindo o tempo do Shell Sort com a sequência Hibbard
        inicio_hibbard = time.time()
        shell_sort_hibbard(lista.copy())
        tempo_hibbard = time.time() - inicio_hibbard

        print(f"Tamanho da lista: {tamanho}")
        print(f"Tempo do Shell Sort (Shell): {tempo_shell:.6f} segundos")
        print(f"Tempo do Shell Sort (Knuth): {tempo_knuth:.6f} segundos")
        print(f"Tempo do Shell Sort (Hibbard): {tempo_hibbard:.6f} segundos")
        print("-" * 40)

# Executa a comparação de desempenho
comparar_shell_sort()
