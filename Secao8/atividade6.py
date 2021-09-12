#entradas e variaveis
valor = int(input("Digite os valores: "))
multiplicar = 0
for n in range(1, 11):
    multiplicar = valor * n
    print(valor, " x ", n, " = ", multiplicar)