class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.__saldo = saldo  # saldo é privado
        self.transacoes = []

    def depositar(self, valor):
        self.__saldo += valor
        self.registrar_transacao("Depósito", valor)
    
    def sacar(self, valor): 
        if valor <= self.saldo_disponivel():
            self.__saldo -= valor
            self.registrar_transacao("Saque", valor)
        else:
            print("Saldo insuficiente.")
    
    def consultar_saldo(self):
        print("Saldo:", self.get_saldo())
    
    def get_saldo(self):
        return self.__saldo
    
    # Setter para alterar o saldo
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("O saldo não pode ser negativo.")
    
    def saldo_disponivel(self):
        return self.get_saldo()

    def registrar_transacao(self, tipo, valor):
        self.transacoes.append({"Tipo": tipo, "Valor": valor})

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, limite_cheque_especial=0):
        super().__init__(numero_conta)
        self.limite_cheque_especial = limite_cheque_especial
    
    # Saque com limite considerando o cheque especial
    def sacar(self, valor):
        if valor <= self.saldo_disponivel() + self.limite_cheque_especial:
            self.set_saldo(self.get_saldo() - valor)
            self.registrar_transacao("Saque", valor)
        else:
            print("Limite de saque excedido. Saldo + cheque especial não são suficientes.")

    def emitir_cheque(self, valor):
        if self.get_saldo() + self.limite_cheque_especial >= valor:
            self.set_saldo(self.get_saldo() - valor)
            self.registrar_transacao("Emissão de Cheque", valor)
        else:
            print("Limite de cheque especial excedido.")

class ContaPoupanca(ContaBancaria):
    def calcular_juros_mensal(self, taxa_juros):
        juros = self.get_saldo() * (taxa_juros / 100)
        self.set_saldo(self.get_saldo() + juros)
        self.registrar_transacao("Juros Mensais", juros)

class ContaInvestimento(ContaBancaria):
    def __init__(self, numero_conta):
        super().__init__(numero_conta)
        self.investimentos = []
    
    def realizar_investimento(self, produto, valor):
        # Lógica para realizar o investimento
        self.registrar_transacao("Investimento", valor)

minha_conta = ContaBancaria(numero_conta="12345")
minha_conta.depositar(100)
minha_conta.consultar_saldo()
