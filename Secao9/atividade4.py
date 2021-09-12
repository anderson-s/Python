#variaveis
vetor = []
soma = 0

#Entrada/Processamento

for n in range(1, 21):
    num = int(input("Digite um valor para o vetor"))
    vetor.append(num)
    # soma = num + soma
print("A soma do vetor é {0}".format(sum(vetor)))

# for n in vetor:
#     print(n)
# print(soma)