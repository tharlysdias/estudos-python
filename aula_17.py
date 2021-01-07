# Polimorfismo == Multiplas formas/ Multiplos Comportamentos
class ContaBancaria(object):
    # Metodo init constroi a nossa classe
    def __init__(self):
        self.saldo = 0
        self.conexao = "http://meusite.com.br:3006"
    
    def depositar(self, valor):
        print("Depositar da super classe")
        self.saldo += valor
        self.consultar_saldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.consultar_saldo()

    def consultar_saldo(self):
        print(self.saldo)

    # Metodo Destrutor
    def __del__(self):
        print("Fechando conexao com o banco de dados em segurança")
        self.conexao = None


class ContaPoupanca(ContaBancaria):
    rentabilidade_total = 1.6

    # metodo privado
    def _consulta_rentabilidade(self):
        return self.rentabilidade_total
        
    def rentabilidade(self):
        rentabilidade = self._consulta_rentabilidade()

        if rentabilidade < 0.5:
            print("Consulte seu gerente")
        else:
            print(rentabilidade)

    # Override (sobrescrever) de metodos
    def depositar(self, valor):
        self.saldo += valor

        if self.saldo >= 1000:
            self.rentabilidade_total += 0.1
            print("Parabéns sua rentabilidade aumentou para: ")
            self.rentabilidade()

# Polimorfismo
class ContaCorrente(ContaBancaria):
    def depositar(self, valor):
        if valor < 100:
            raise Exception("Valor minimo é de R$ 100")
        else:
            # Metodo super
            super(ContaCorrente, self).depositar(valor)
            """
            Ao invés do super, também pode ser feito assim:
            self.saldo += valor
        self.consultar_saldo()"""

conta_poupanca = ContaPoupanca()
conta_poupanca.rentabilidade()
conta_poupanca.depositar(1000)
conta_poupanca.sacar(50)
conta_poupanca.consultar_saldo()

conta_corrente = ContaCorrente()
conta_corrente.depositar(100)