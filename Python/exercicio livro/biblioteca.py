from models.livro import Livro

livro1 = Livro('EL', 'Elder', 1984)
livro2 = Livro('JV', 'João', 1984)
livro3 = Livro('SW', 'Swellen', 1994)
livro4 = Livro('OS', 'Elder', 2004)

Livro.verificar_disponibilidade(1984)
Livro.emprestar(livro2)
Livro.listar_livros()
Livro.verificar_disponibilidade(1984)

def main():
    Livro.listar_livros


if __name__ == '__main__':
    main()