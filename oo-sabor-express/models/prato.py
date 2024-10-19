from models.item_cardapio import ItemCardapio

class Prato(ItemCardapio):#Está herdando de ItemCardapio
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)#Está utilizando os atributos do construtor da classe pai
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    @property
    def descricao(self):
        return self._descricao
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)