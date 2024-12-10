import time

# Função do Ternary Search
def ternary_search(lista, baixo, alto, alvo):
    if baixo <= alto:
        # Calculando os dois pontos de divisão
        mid1 = baixo + (alto - baixo) // 3
        mid2 = alto - (alto - baixo) // 3

        # Verificar se o alvo está nos pontos de divisão
        if lista[mid1] == alvo:
            return mid1
        if lista[mid2] == alvo:
            return mid2

        # Se o alvo for menor que o primeiro ponto de divisão, buscar na primeira parte
        if alvo < lista[mid1]:
            return ternary_search(lista, baixo, mid1 - 1, alvo)
        # Se o alvo for maior que o segundo ponto de divisão, buscar na última parte
        elif alvo > lista[mid2]:
            return ternary_search(lista, mid2 + 1, alto, alvo)
        # Caso contrário, buscar na parte do meio
        else:
            return ternary_search(lista, mid1 + 1, mid2 - 1, alvo)

    # Caso o alvo não seja encontrado
    return -1

# Função do Binary Search
def binary_search(lista, baixo, alto, alvo):
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

# Função para comparar o desempenho do Ternary Search e Binary Search
def comparar_desempenho():
    tamanhos = [10**3, 10**4, 10**5]
    alvo = 500  # Alvo de teste

    for tamanho in tamanhos:
        lista = list(range(tamanho))

        # Medindo o tempo do Ternary Search
        inicio_ternary = time.time()
        ternary_search(lista, 0, len(lista) - 1, alvo)
        tempo_ternary = time.time() - inicio_ternary

        # Medindo o tempo do Binary Search
        inicio_binary = time.time()
        binary_search(lista, 0, len(lista) - 1, alvo)
        tempo_binary = time.time() - inicio_binary

        print(f"Tamanho da lista: {tamanho}")
        print(f"Tempo do Ternary Search: {tempo_ternary:.6f} segundos")
        print(f"Tempo do Binary Search: {tempo_binary:.6f} segundos")
        print("-" * 40)

# Executa a comparação de desempenho
comparar_desempenho()
