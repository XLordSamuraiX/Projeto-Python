texto = input("Informe um texto: ")
vogais = "AEIOU"

# Exemplo utilizando um interável
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end = "")

print()

# Exemplo utilizando a função built-in range
for numero in range(0,51,5):
    print(numero, end = " ")

# Exemplo utilizando o while
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato  \n[0] Sair  \n: "))

    if opcao == 1:
        print("Sacando....")
    
    elif opcao == 2:
        print("Exibindo o extrato...")

    else:
        print("Obrigado por usar nosso sistema bancário, atá logo!")
