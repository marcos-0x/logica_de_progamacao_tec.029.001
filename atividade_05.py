nome = input("Digite seu nome: ").strip().title()
nota1 = int(input("Digite sua primeira nota: ")) 
nota2 = int(input("Digite sua segunda nota: "))
media = (nota1 + nota2)/2
# se o usuario tirar nota quebrada programa quebra :(

print(f"Média {media}")
if media >= 7:
    print(f"{nome} está aprovado")
elif media >= 5:
    print(f"{nome} está de recuperação")
else:
    print(f"{nome} está reprovado")