nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
if media >=7 :
    print("A média final do aluno é: {0:.2f}.".format(media), "O aluno e está aprovado!")
elif media < 7 and media >= 5:
    print("A média final do aluno é: {0:.2f}".format(media), "O aluno está na recuperação!")
elif media < 5:
    print("A média final do aluno é: {0:.2f}".format(media), "O aluno está reprovado!")

