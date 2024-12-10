def binary_search_recursive(sorted_list, target, left, right):
    if left > right:
        return -1  # Caso base: elemento não encontrado

    mid = (left + right) // 2  # Calcula o índice do meio

    if sorted_list[mid] == target:
        return mid  # Retorna o índice se o elemento foi encontrado
    elif sorted_list[mid] < target:
        return binary_search_recursive(sorted_list, target, mid + 1, right)  # Busca à direita
    else:
        return binary_search_recursive(sorted_list, target, left, mid - 1)  # Busca à esquerda


# Testando o algoritmo com outra lista
sorted_list = [2, 4, 8, 16, 32, 64, 128]
target = 32

# Chamada inicial com os limites esquerdo e direito
result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
if result != -1:
    print(f"O número {target} foi encontrado no índice {result}.")
else:
    print(f"O número {target} não está na lista.")
