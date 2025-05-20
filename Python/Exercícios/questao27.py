def criar_senha():
    while True:
        senha = input("Digite a senha: ")
        confirmacao = input("Confirme a senha: ")

        if senha == confirmacao:
            print("Senha criada com sucesso.")
            break
        else:
            print("As senhas não coincidem. Tente novamente.")

criar_senha()