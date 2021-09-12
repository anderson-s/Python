#Entrada
poluicao = float(input("Digite o valor: "))

#Processamento

if poluicao < 0.3:
    print("Níveis aceitáveis")
elif poluicao >= 0.3 and poluicao < 0.4:
    print("Grupo 1 - Suspender atividades")
elif poluicao >= 0.4 and poluicao < 0.5:
    print("Grupo 1 e 2 - Suspender atividades")
elif poluicao >= 0.5:
    print("Todos os grupos com atividades paralisadas")