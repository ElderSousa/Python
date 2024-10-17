
class Livro:

    livros = []
    def __init__(self, titulo, autor, ano_publicacao=0, disponivel=True):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = disponivel
        Livro.livros.append(self)

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        self._titulo = value
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, value):
        self._autor = value
    
    @property
    def ano_publicacao(self):
        return self._ano_publicacao
    
    @ano_publicacao.setter
    def ano_publicacao(self, value):
        self._ano_publicacao = value
    
    @property
    def disponivel(self):
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, value):
        self._disponivel = value

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}'
    
    def emprestar(self):
        self.disponivel = False

    @classmethod
    def listar_livros(cls):
        print(f"{'Titulo'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano de publicação'.ljust(25)} | {'Status'}")
        for livro in cls.livros:
            print(f'{livro.titulo.ljust(25)} | {livro.autor.ljust(25)} | {str(livro.ano_publicacao).ljust(25)} | {livro.disponivel}')

    @staticmethod
    def verificar_disponibilidade(ano):
        print('Lista de livros do ano solicitado: ')
        if ano != Livro.ano_publicacao:
            return Livro.livros.__sizeof__
        else:
            Livro.listar_livros()
            
livro1 = Livro('primeiro', 'elder', 1984 )
livro2 = Livro('segundo', 'jv', 1984 )
livro3 = Livro('terceiro', 'sw', 1994 )
Livro.listar_livros()
Livro.verificar_disponibilidade(1984)
