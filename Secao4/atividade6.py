#Entrada
valor = float(input("Digite o valor que você recebe por hora: "))
horas = int(input("Digite quantas horas você trabalhou no mês: "))
#Processamento
salario = valor * horas
#Saída
print("O seu salário vai ser de R$ {0:.2f}".format(salario))