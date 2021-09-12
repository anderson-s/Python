#Entrada
p = float(input("Digite o valor: "))
#Processamento
if p > 50:
    e = p - 50
    m = e * 4
else:
    e = 0
    m = 0
print("O excesso foi de {0:.2f}kg, então a multa corresponde a R$: {1:.2f}".format(e, m))
