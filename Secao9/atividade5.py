#variaveis
vetor = []
aux = False

for n in range(0, 10):
    num = int(input("Digite um valor para o vetor"))
    vetor.append(num)
for n in vetor:
    if n > 50:
        print("O número {0} maior que 50 na posição: {1}".format(n, vetor.index(n)))
        aux = True
if aux == False:
    print("não existem valores maiores que 50")