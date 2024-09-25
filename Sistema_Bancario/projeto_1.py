saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saques = 3

print("Bem-Vindo ao Banco-Python!!!")

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

while True:

    print("Selecione umas das opções abaixo:")

    opcao = float(input(menu))

if opcao == 1:
    x = float(input("Quanto deseja depositar?"))
    if x > 0:
        saldo += x
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print(f"O saldo atua é de R${saldo}")
    else:
        print("Valor do depósito inválido.")


elif opcao == 2:
    x = float(input("Quanto deseja sacar?"))
    if saldo == 0:
        print("Não foi possível sacar, por falta de saldo em conta.")

    elif numero_saque == 3:
        print("Você já atingiu o limite de saques do dia.")

    else:
        if (saldo >= x) and (x <= 500) and (x>0):
            numero_saque += 1
            saldo -= x
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print(f"Saque efetuado. O saldo atua é de R${saldo}")
    

elif opcao == 3:
     print("=== Extrato ===")
     if extrato:
         print(extrato)
     else:
        print("Não foram realizadas movimentações.")
        print(f"Saldo atual: R${saldo:.2f}")


elif opcao == 0:
    print("Saindo... Até mais!")
    break


else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")