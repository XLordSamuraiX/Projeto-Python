maior_idade = 18
idade_especial = 17

idade = int(input("Informe sua idade: "))

#Exemplo 1:
if idade >= maior_idade:
    print("Maior de idade, pode tirar CNH.")

if idade <maior_idade:
    print("Ainda não pode tirar a CNH.")

# Exemplo 2:
if idade >= maior_idade:
    print("Maior de idade, pode tirar CNH.")

else:
    print("Ainda não pode tirar a CNH.")

# Exemplo 3:
if idade >= maior_idade:
    print("Maior de idade, pode tirar CNH.")

elif idade == idade_especial:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")

else:
    print("Ainda não pode tirar a CNH.")

# Estrutura condicional ternária
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")