#entradas e variaveis
maior = -999999
menor = 9999999
soma = 0

for n in range(1, 11):
    valor = int(input("Digite os valores: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = valor + soma
    else:
        valor = int(input("Digite os valores: "))
media = soma/10
print("A média equivale a:", media)
print("A maior número foi:", maior)
print("O menor número foi:", menor)
