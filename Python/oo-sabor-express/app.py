from models.restaurante import Restaurante#Faz a importção de restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
#restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
#restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)
def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()