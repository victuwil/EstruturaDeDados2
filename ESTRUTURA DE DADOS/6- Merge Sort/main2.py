def merge_sort(lista):
    # Caso base: se a lista tem 1 ou menos elementos, já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Dividir a lista ao meio
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Recursivamente ordenar as metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    # Combinar as listas ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    # Ordenar os elementos enquanto há itens em ambas as listas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:  # Comparação lexicográfica entre strings
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adicionar o que restou de cada lista (se houver)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

# Testando o Merge Sort com strings
lista = ["banana", "maçã", "laranja", "abacaxi", "kiwi", "morango"]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)
