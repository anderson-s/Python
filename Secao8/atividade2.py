#Entrada
for n in range(1, 101):
    if n % 10 == 0:
        aux = "Múltipo de 10"
    else:
        aux = ""
    print(n, aux)