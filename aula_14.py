# Orientação a objetos
"""
classe
objeto
construtor
metodos
atributos
herança

sobrecarga de metodos
pomorfismo
destrutores
"""

# definição da classe
# henraça do object
class Casa(object):
    # atributos e valores da classe
    cor = "Amarela"
    altura = 3
    quartos = 10

    # construtor
    def __init__(self, cor, altura, quartos):
        self.cor = cor
        self.altura = altura
        self.quartos = quartos

    # Metodos e Construtores
    # uma classe pode ter vários metodos
    def pintar(self, cor):
        self.cor = cor

    def aumenta_quartos(self, quartos):
        self.quartos = quartos

    def imprime_casa(self):
        print(self.cor, self.altura, self.quartos)

# obejto criada atráves da instancia
minha_casa = Casa("Vermelha", 10, 2)
minha_casa.imprime_casa()

minha_casa.pintar("Verde")
minha_casa.aumenta_quartos(9)
minha_casa.imprime_casa()

# acessando os objetos e atributos
print(minha_casa.cor, minha_casa.altura)

# chamando o metodo
minha_casa.pintar("Roxa")
print(minha_casa.cor)

minha_casa.aumenta_quartos(7)
print(minha_casa.quartos)