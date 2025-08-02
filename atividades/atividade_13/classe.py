class Conta:
    # Construtor
    def __init__(self, titular, cpf, agencia, numero_da_conta, saldo):
        # Atributos da classe
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    # Metódo de ação
    def consultar_dados(self):
        print(f"Titular: {self.titular}\nCPF: {self.cpf}\nAgência: {self.agencia}\Número da conta: {self.numero_da_conta}\nSaldo: {self.saldo}")




      