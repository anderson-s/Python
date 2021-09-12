nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while nome == senha:
    print("A senha não pode ser idêntica ao nome")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
