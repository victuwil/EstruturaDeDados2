def binary_search(lista, palavra):
    low = 0
    high = len(lista) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_palavra = lista[mid].lower()  # Comparação case-insensitive
        
        if mid_palavra == palavra.lower():  # Palavra encontrada
            return True
        elif mid_palavra < palavra.lower():  # Palavra está à direita
            low = mid + 1
        else:  # Palavra está à esquerda
            high = mid - 1
            
    return False  # Palavra não encontrada

# Exemplo de uso
palavras = ["abacaxi", "banana", "laranja", "maçã"]
palavra_a_buscar = "banana"

if binary_search(palavras, palavra_a_buscar):
    print(f'A palavra "{palavra_a_buscar}" está presente na lista.')
else:
    print(f'A palavra "{palavra_a_buscar}" não está presente na lista.')
