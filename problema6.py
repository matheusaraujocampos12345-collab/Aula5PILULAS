from conta import ContaBancaria

conta1 = ContaBancaria('Alcides', 30000)
conta2 = ContaBancaria('Maria', 2000.50)

conta1.exibir_saldo()
conta1.depositar(1000000)
conta1.exibir_saldo()
conta1.sacar(100000)
conta1.sacar(14000)
conta1.exibir_saldo()

contas = []
for i in range(5):
    nome = input('Nome')
    saldo = float(input('Saldo:'))
    contas.append(ContaBancaria(nome,saldo))
    
for conta in contas:
    print(f'{conta.titular} R$ {conta.saldo }')