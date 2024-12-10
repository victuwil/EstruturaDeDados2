# Lista de alunos com notas
alunos = [("Alice", 70), ("Bob", 85), ("Carlos", 70), ("Diana", 60)]

# Função Bubble Sort (Estável)
def bubble_sort_stable(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j][1] > lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Função Quick Sort (Instável)
def quick_sort_unstable(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0][1]
    left = [x for x in lista[1:] if x[1] < pivot]
    right = [x for x in lista[1:] if x[1] >= pivot]
    return quick_sort_unstable(left) + [lista[0]] + quick_sort_unstable(right)

# Bubble Sort (Estável)
alunos_bubble = alunos.copy()
bubble_sort_stable(alunos_bubble)
print("Bubble Sort (Estável):", alunos_bubble)

# Quick Sort (Instável)
alunos_quick = alunos.copy()
alunos_quick = quick_sort_unstable(alunos_quick)
print("Quick Sort (Instável):", alunos_quick)
