conta_criada = False
nome = ""
conta = ""
saldo = 0.0

while True:
    print("\n1- Criar Conta | 2- Depositar | 3- Sacar | 4- Extrato/Ver Saldo | 5- Sair")
    opcao = input("Opção: ")
    
    if opcao == '1':
        nome = input("Nome do titular: ")
        conta = input("Número da conta: ")
        saldo = float(input("Saldo inicial: "))
        conta_criada = True
        print("Conta criada com sucesso!")
    elif opcao == '2':
        if not conta_criada:
            print("Crie uma conta primeiro!")
        else:
            valor = float(input("Valor do depósito: R$ "))
            saldo += valor
            print("Depósito realizado!")
    elif opcao == '3':
        if not conta_criada:
            print("Crie uma conta primeiro!")
        else:
            valor = float(input("Valor do saque: R$ "))
            if valor <= saldo:
                saldo -= valor
                print("Saque realizado!")
            else:
                print("Saldo insuficiente!")
    elif opcao == '4':
        if not conta_criada:
            print("Crie uma conta primeiro!")
        else:
            print(f"\nTitular: {nome} | Conta: {conta} | Saldo: R$ {saldo:.2f}")
    elif opcao == '5':
        break