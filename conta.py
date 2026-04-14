class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R$ {valor} realizado.')
        
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'O valor de {valor} foi debitado')
        else:
            print('Sem grana')
    
    def exibir_saldo(self):
        print(f'Saldo atual Titular {self.titular} R$ {self.saldo}')