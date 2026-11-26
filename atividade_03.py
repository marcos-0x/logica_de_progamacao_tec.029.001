nome = input("Digite seu nome: ").strip().title()
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")
