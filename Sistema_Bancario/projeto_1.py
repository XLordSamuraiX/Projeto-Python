from datetime import datetime

saldo = 0
limite = 1000
extrato = ""
numero_saque = 0
limite_saques = 10
mascara_ptbr = "%d/%m/%Y %H:%M"
agencia = "0001"
contas = []
usuarios = []

def deposito(saldo, extrato, x):
    if x > 0:
        saldo += x
        data_hora_str = datetime.now()  # Obter a data e hora atual
        tempo = data_hora_str.strftime(mascara_ptbr)
        extrato += f"Depósito: R${x:.2f} - Data: {tempo}\n"
        print(f"O saldo atual é de R${saldo:.2f}")
    else:
        print("Valor do depósito inválido.")

    return saldo, extrato

def saque(saldo, extrato, limite, numero_saque, limite_saques, x):
    if saldo == 0:
        print("Não foi possível sacar, por falta de saldo em conta.")
    elif numero_saque >= limite_saques:
        print("Você já atingiu o limite de saques do dia.")
    else:
        if (saldo >= x) and (x <= limite) and (x > 0):
            numero_saque += 1
            saldo -= x
            data_hora_str = datetime.now()  # Obter a data e hora atual
            tempo = data_hora_str.strftime(mascara_ptbr)
            extrato += f"Saque: R${x:.2f} - Data: {tempo}\n"
            print(f"Saque efetuado. O saldo atual é de R${saldo:.2f}")
        else:
            print("Valor de saque inválido ou maior que o saldo disponível.")
    
    return saldo, extrato, numero_saque

def exibir_extrato(saldo, extrato):
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"Saldo atual: R${saldo:.2f}\n")

def criar_usuario(usuarios):
    cpf = input("Informe seu cpf:")
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe usuário com esse CPF.")


    nome = input("Informe seu nome:")
    data_nascimento = input("Informe sua data de nasacimento:")
    endereco = input("Informe seu endereco:")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario cria com sucesso")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu cpf:")
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe usuário com esse CPF.")

    if usuarios:
        print("Conta criada com sucesso!!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario não encontrato, erro de criacao de conta.")



print("Bem-Vindo ao Banco-Python!!!")

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Criar Usuário
[0] Sair
"""

opcao = -1  # Inicializando a variável opcao

while opcao != '0':
    print("Selecione uma das opções abaixo:")
    opcao = input(menu)

    if opcao == '1':
        x = float(input("Quanto deseja depositar? "))
        saldo, extrato = deposito(saldo, extrato, x) 

    elif opcao == '2':
        x = float(input("Quanto deseja sacar? "))
        saldo, extrato, numero_saque = saque(saldo, extrato, limite, numero_saque, limite_saques, x)

    elif opcao == '3':
        print("=== Extrato ===")
        exibir_extrato(saldo, extrato)

    elif opcao == '4':
        numero_conta = len(contas) + 1
        conta = criar_conta(agencia, numero_conta, usuarios)

        if conta:
            contas.append(conta)


    elif opcao == '5':
        criar_usuario(usuarios)

    elif opcao == '0':
        print("Saindo... Até mais!")
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")