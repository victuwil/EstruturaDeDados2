import math

# Função de ordenação usando o Bucket Sort
def bucket_sort(lista):
    # Passo 1: Criação dos baldes
    n = len(lista)
    if n <= 1:
        return lista
    
    # Criando os baldes
    baldes = [[] for _ in range(n)]
    
    # Passo 2: Distribuição dos elementos nos baldes
    for num in lista:
        # O índice de um balde é determinado multiplicando o valor pelo número de baldes
        indice = math.floor(num * n)
        baldes[indice].append(num)
    
    # Passo 3: Ordenação de cada balde (usando Insertion Sort para simplificar)
    for balde in baldes:
        balde.sort()  # Alternativamente, pode-se usar qualquer outro algoritmo de ordenação
    
    # Passo 4: Concatenar todos os baldes
    resultado = []
    for balde in baldes:
        resultado.extend(balde)
    
    return resultado

# Função para testar o Bucket Sort
def testar_bucket_sort():
    lista = [0.78, 0.17, 0.39, 0.55, 0.92, 0.23, 0.68, 0.34, 0.80, 0.87]
    print("Lista antes da ordenação:")
    print(lista)
    
    lista_ordenada = bucket_sort(lista)
    
    print("Lista após a ordenação:")
    print(lista_ordenada)

# Executa o teste
testar_bucket_sort()
