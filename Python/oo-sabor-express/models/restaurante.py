from models.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):#construtor
        self._nome = nome.title()#Deixa a primeira letra do nome maiúscula
        self._categoria = categoria.upper()#Deixa a string com todas as letras maiúsculas.
        self._ativo = False#Propriedade protegido para que náo possa ser modificado de forma direta, e sim por método.
        self._avaliacao = []#Composição de objetos
        Restaurante.restaurantes.append(self)#Lista adicionará o objeto referênciado


    def __str__(self):#É a referência da instância atual que estamos usando, esse método transforma o objeto em uma string.
        return f'{self._nome} | {self._categoria}'
    
    @classmethod#Annotação usada para informar que o método é da classe e terá que ser usado o 'cls' como parâmetro.
    def listar_restaurante(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")#Para formatar e usar ljust com string utilizar aspas "".
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')#ljust() cria espaçamento entre os valores exibidos.

    @property#Modifica como o atributo é lido.
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)#Média com apenas uma casa decimal
        return media

