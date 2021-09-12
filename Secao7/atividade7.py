#Entrada
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))

#Processamento
p1 = a * a
p2 = b * b
p3 = c * c
p4 = d * d
if p3 >= 1000:
    print(p3)
else:
    print("O quadrado de ", a, " é = ", p1,"\nO quadrado de ", b, " é = ", p2,
    "\nO quadrado de ", c, " é = ", p3,
    "\nO quadrado de ", d, " é = ", p4)
