massa = float(input("Digise sua massa: ").replace(',','.'))
altura = float(input("Digite sua altura").replace(',','.'))

if massa <= 140 and altura >= 1.75: 
	print("Entrada do usuário permitida.")
else:
	print("Entrada do usuário negada.")