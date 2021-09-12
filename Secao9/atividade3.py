#variaveis
vetor = []

#Entrada/Processamento

for n in range(0, 10):
    num = int(input("Digite um valor para o vetor"))
    vetor.append(num)
vetor.reverse()
for n in vetor:
    print(n)