class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn})"


def binary_search_livro(lista, isbn):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_isbn = lista[mid].isbn  # Acessa o ISBN do livro no meio da lista

        if mid_isbn == isbn:
            return lista[mid]  # Retorna o livro encontrado
        elif mid_isbn < isbn:
            low = mid + 1  # Pesquisa na metade direita
        else:
            high = mid - 1  # Pesquisa na metade esquerda

    return None  # Livro não encontrado


# Exemplo de lista de livros ordenada por ISBN
livros = [
    Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 9780261103573),
    Livro("1984", "George Orwell", 9780451524935),
    Livro("Dom Casmurro", "Machado de Assis", 9788535910851),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 9788535900777)
]

# ISBN que queremos procurar
isbn_a_procurar = 9780451524935

# Procurar o livro usando o Binary Search
livro_encontrado = binary_search_livro(livros, isbn_a_procurar)

if livro_encontrado:
    print(f'Livro encontrado: {livro_encontrado}')
else:
    print("Livro não encontrado.")
