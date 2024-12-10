# Função de Pesquisa Interpolada
def interpolation_search(sorted_list, target):
    start = 0
    end = len(sorted_list) - 1

    while start <= end and target >= sorted_list[start] and target <= sorted_list[end]:
        # Calcula a posição estimada usando interpolação
        pos = start + ((target - sorted_list[start]) * (end - start)) // (sorted_list[end] - sorted_list[start])

        # Verifica se o valor foi encontrado
        if sorted_list[pos] == target:
            return pos
        # Ajusta o intervalo da busca
        elif sorted_list[pos] < target:
            start = pos + 1
        else:
            end = pos - 1

    return -1  # Retorna -1 se o elemento não for encontrado


# Função de Pesquisa Binária
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2  # Calcula o índice do meio
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Listas de teste
uniform_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
non_uniform_list = [1, 4, 9, 25, 36, 100, 225, 400]

# Testando ambas as funções em listas uniformes e não uniformes
print("### Teste em lista uniforme ###")
print("Interpolation Search:", interpolation_search(uniform_list, 35))  # Deve retornar 6
print("Binary Search:", binary_search(uniform_list, 35))  # Deve retornar 6

print("\n### Teste em lista não uniforme ###")
print("Interpolation Search:", interpolation_search(non_uniform_list, 36))  # Deve retornar 4
print("Binary Search:", binary_search(non_uniform_list, 36))  # Deve retornar 4

print("\n### Teste para valores inexistentes ###")
print("Interpolation Search:", interpolation_search(uniform_list, 100))  # Deve retornar -1
print("Binary Search:", binary_search(uniform_list, 100))  # Deve retornar -1
