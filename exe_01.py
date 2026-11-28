valor_gasolina = float(input("Digite o valor da gasolina: ").replace(',','.'))
valor_etanol = float(input("Digite o valor do etanol: ").replace(',','.'))

if valor_etanol <= valor_gasolina * 0.75:
    print("Compensa mais abastecer com etanol")
else:
    print("Compensa abastecer com gasolina")
