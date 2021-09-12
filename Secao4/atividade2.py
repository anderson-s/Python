#Declarando e recebendo valores nas variáveis
quantidade_minima = int(input("Digite a quantidade minima: "))
quantidade_maxima = int(input("Digite a quantidade maxima: "))
#Processamento
estoque_medio = (quantidade_maxima + quantidade_minima)/2
#Saída
print("O estoque médio é: {0}".format(estoque_medio))