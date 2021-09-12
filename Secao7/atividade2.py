#Entrada
n = int(input("Digite o valor: "))
#Processamento
if(n > 0):
    a = n
    print("O valor {0} é positivo".format(a))
elif(n < 0):
    b = n
    #Saída
    print("O valor {0} é negativo".format(b))
elif(n == 0):
    c = n
    print("O valor {0} é nulo".format(c))