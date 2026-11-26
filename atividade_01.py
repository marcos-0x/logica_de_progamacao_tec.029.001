# Início
nome = input("Digite seu nome: ").strip().title()
email = input("Digite seu email: ").strip().lower()
cpf = input("Digite seu cpf: " ).strip()
telefone = input("Digite seu telefone: ").strip()
idade = int(input("Digite sua idade "))
altura = float(input("Digite sua altura: ").replace(',', '.'))

print(f"Nome: {nome}") 
print(f"E-,3mail: {email}") 
print(f"CPF: {cpf}") 
print(f"Telefone: {telefone}")  
print(f"Anos: {idade}") 
print(f"Altura: {altura}")  