import random

# Definindo a classe do aluno
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"{self.nome}: {self.nota}"

# Função para realizar o Bucket Sort
def bucket_sort(lista):
    # Verificar se a lista está vazia
    if len(lista) == 0:
        return lista

    # Criar baldes (buckets) com intervalos [0-100]
    n = len(lista)
    min_val = 0
    max_val = 100
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]

    # Preencher os baldes
    for aluno in lista:
        index = int(aluno.nota / 10)
        if index == bucket_count:
            index -= 1
        buckets[index].append(aluno)

    # Ordenar dentro de cada balde
    for bucket in buckets:
        bucket.sort(key=lambda aluno: aluno.nota)

    # Concatenar todos os baldes em uma lista ordenada
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(bucket)

    return sorted_list

# Função de Interpolation Search
def interpolation_search(lista, nota):
    low = 0
    high = len(lista) - 1

    while low <= high and lista[low].nota <= nota <= lista[high].nota:
        # Interpolation Formula
        pos = low + int(((nota - lista[low].nota) * (high - low)) / (lista[high].nota - lista[low].nota))

        # Verificar se o valor procurado foi encontrado
        if lista[pos].nota == nota:
            return lista[pos]
        elif lista[pos].nota < nota:
            low = pos + 1
        else:
            high = pos - 1

    return None  # Nota não encontrada

# Teste do código com alunos
def testar_algoritmos():
    # Criar uma lista de alunos com notas aleatórias entre 0 e 100
    alunos = [
        Aluno("Alice", random.uniform(0, 100)),
        Aluno("Bob", random.uniform(0, 100)),
        Aluno("Carlos", random.uniform(0, 100)),
        Aluno("Diana", random.uniform(0, 100)),
        Aluno("Eva", random.uniform(0, 100)),
        Aluno("Felipe", random.uniform(0, 100)),
        Aluno("Gabriela", random.uniform(0, 100)),
        Aluno("Hugo", random.uniform(0, 100)),
        Aluno("Irene", random.uniform(0, 100)),
        Aluno("João", random.uniform(0, 100)),
    ]

    # Exibir alunos antes da ordenação
    print("Alunos antes da ordenação:")
    for aluno in alunos:
        print(aluno)

    # Ordenar os alunos por suas notas
    alunos_ordenados = bucket_sort(alunos)

    # Exibir alunos após a ordenação
    print("\nAlunos ordenados:")
    for aluno in alunos_ordenados:
        print(aluno)

    # Nota que queremos procurar
    nota_a_procurar = alunos_ordenados[5].nota  # Procurar a nota do aluno na posição 5

    # Realizando a busca pelo aluno com Interpolation Search
    aluno_encontrado = interpolation_search(alunos_ordenados, nota_a_procurar)

    # Exibir o resultado da busca
    if aluno_encontrado:
        print(f"\nAluno encontrado: {aluno_encontrado}")
    else:
        print("\nAluno não encontrado.")

# Executando os testes
testar_algoritmos()
