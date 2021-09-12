#Variáveis e Entradas
altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: M/F: ")
#Processamento
#lower() --> vai converter as letras para minusculo
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
    print("O seu peso ideal é {0:.2f}kg".format(peso_ideal))
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print("O seu peso ideal é {0:.2f}kg".format(peso_ideal))
else:
    print("Sexo não definido")