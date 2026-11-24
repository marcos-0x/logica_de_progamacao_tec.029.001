# entrada de dados
nome = input("Informe o nome: ")
idade = input("Informe sua idade: ")
altura = float(input("Digite sua altura: ").replace(",", "."))

# conversão de tipo
idade = int(idade)
altura = float(altura)


# saída de dados
print(f"Nome: {nome}. Tipo: {type(nome)}")
print(f"Idade: {idade}. Tipo: {type(idade)}")
print(f"Altura: {altura}. Tipo: {type(altura)}")
