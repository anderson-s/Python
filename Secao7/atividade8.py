#Entrada
a = int(input("Digite o valor: "))

#Processamento

if a % 2 == 0:
    if a > 0:
        print("O valor é positivo e par")
    else:
        print("O valor é negativo e par")
else:
    if a > 0:
        print("O valor é impar e positivo")
    else:
        print("O valor é negativo e impar")