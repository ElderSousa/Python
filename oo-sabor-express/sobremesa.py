from models.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao
    
    def __str__(self):
        return f'{super().__str__(), {self._tipo}, {self._tamanho}, {self._descricao}}'
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def tamanho(self):
        return self._tamanho
    
    @property
    def descricao(self):
        return self._descricao
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15) 