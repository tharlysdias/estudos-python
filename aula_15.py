# Herança e metodos privados
class ContaBancaria(object):
    def __init__(self):
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
        self.consultar_saldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.consultar_saldo()

    def consultar_saldo(self):
        print(self.saldo)


class ContaPoupanca(ContaBancaria):
    def _consulta_rentabilidade(self):
        return 1.6
        
    def rentabilidade(self):
        rentabilidade = self._consulta_rentabilidade()

        if rentabilidade < 0.5:
            print("Consulte seu gerente")
        else:
            print(rentabilidade)


conta_poupanca = ContaPoupanca()
conta_poupanca.rentabilidade()
conta_poupanca.depositar(100)
conta_poupanca.sacar(50)
conta_poupanca.consultar_saldo()