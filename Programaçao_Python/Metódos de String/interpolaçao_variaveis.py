nome = "Rei"
idade = 27
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Rei", "idade": 27}

print("Nome: %s Idade: %d" % (nome,idade))

print("Nome: {} Idade:{}".format(nome,idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(idade = idade, nome = nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")