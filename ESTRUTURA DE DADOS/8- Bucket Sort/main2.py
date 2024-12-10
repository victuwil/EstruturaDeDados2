import math

# Função de Bucket Sort para números inteiros positivos em intervalos maiores
def bucket_sort_inteiros(lista):
    if not lista:
        return lista

    # Determinar o valor máximo da lista para definir os intervalos dos baldes
    max_valor = max(lista)
    
    # Definir o número de baldes e o intervalo de cada balde
    num_baldes = math.ceil(math.sqrt(len(lista)))  # Número de baldes idealmente proporcional ao tamanho da lista
    intervalo = math.ceil((max_valor + 1) / num_baldes)

    # Passo 1: Criar os baldes
    baldes = [[] for _ in range(num_baldes)]

    # Passo 2: Distribuir os elementos nos baldes
    for num in lista:
        # Calcular em qual balde o número deve cair
        indice_balde = num // intervalo
        baldes[indice_balde].append(num)

    # Passo 3: Ordenar cada balde (usando Insertion Sort ou sort nativo)
    for balde in baldes:
        balde.sort()

    # Passo 4: Concatenar os baldes para formar a lista ordenada
    resultado = []
    for balde in baldes:
        resultado.extend(balde)

    return resultado

# Função para testar o Bucket Sort
def testar_bucket_sort_inteiros():
    lista = [78, 17, 39, 55, 92, 23, 68, 34, 80, 87]
    print("Lista antes da ordenação:")
    print(lista)
    
    lista_ordenada = bucket_sort_inteiros(lista)
    
    print("Lista após a ordenação:")
    print(lista_ordenada)

# Executa o teste
testar_bucket_sort_inteiros()
