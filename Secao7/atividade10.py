#Entrada
idade = int(input("Digite a idade: "))

if idade  < 7:
	print("Não pertence a nenhum grupo")
elif idade  >= 5 and idade  <= 7:
	print("Infantil A")
elif idade  > 7 and idade  <= 11:
	print("Infantil B")
elif idade  > 11 and idade  <= 13:
	print("Juvenil A")
elif idade  > 13 and idade  < 18:
	print("Juvenil B")
elif idade >= 18:
	print("Grupo Adulto")
