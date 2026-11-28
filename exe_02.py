nome = input("Digite seu nome: ").title().strip()
massa = float(input("Digite sua massa: ").replace(',','.'))
altura = float(input("Digite sua altura: ").replace(',','.'))
imc = massa / (altura * altura)

if imc < 18.5:
    print(f"{nome} está no abaixo do peso")
elif imc < 25:
    print(f"{nome} está no peso ideal")
elif imc < 30:
    print(f"{nome} está acima do peso")
elif imc < 35:
    print(f"{nome} está obeso")
elif imc < 40:
    print(f"{nome} está com obesidade nível 2")
else:
    print(f"{nome} está com obesidade mórbida")