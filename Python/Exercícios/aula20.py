class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo 
    
    def depositar(self, valor):
        self.saldo += valor 

    def sacar(self, valor ):
        if valor <= self.saldo:
         self.saldo -= valor
        else:
            print("Saldo insuficiente")
    def exibir_saldo(self):
        print(f"{self.titular} possui R$ {self.saldo} na conta")

conta = ContaBancaria("Mattheus", 500)
conta.exibir_saldo()
conta.depositar(200)
conta.exibir_saldo()
conta.sacar(100)
conta.exibir_saldo()
conta.sacar(800)

