
class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome} | {self.idade} anos | {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    @property
    def saudacao(self):
        return f'Ola´ {self.nome} {self.profissao}' if self.profissao else f'Olá {self.nome}'

    @classmethod
    def listar_pessoa(cls):
        print(f'{cls.nome} | {cls.idade} | {cls.profissao}')

pessoa1 = Pessoa('Elder', 18, 'Desenvolvedor')
pessoa2 = Pessoa('JV', 22)
print(pessoa1)
pessoa1.aniversario()
print(f'Idade atual {pessoa1.idade}')
print(f'{pessoa1.saudacao}\n')
print(pessoa2)
print(pessoa2.saudacao)
