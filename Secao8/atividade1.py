#Entrada
a = -1
maior = 0
#Processamento

while a != 0:
    a = int(input("Digite um valor ou digite 0 para encerrar o programa: "))
    if a > maior:
        maior = a

print("O maior valor digitado foi: {0}".format(maior))