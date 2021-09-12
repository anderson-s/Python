#Entrada
c = int(input("Digite o código: "))
n = int(input("Digite as horas que o operário trabalhou: "))

#Processamento
if n > 50:
    e = (n - 50)*20
    salario_total = (50 * 10) + e
    print("O salário total é: R$ {0:.2f}; O salario excesso é: R$ {1:.2f}".format(salario_total, e))
else:
    e = 0
    salario_total = n * 10 
    print("O salário total é: R$ {0:.2f}; O salario excesso é: R$ {1:.2f}".format(salario_total, e))
