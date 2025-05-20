def senha_loop():
    while True:
        senha= input("Digite a senha: ")
        if senha == "senac123":
           print("Acesso liberado!")
           break
        else:
            print("Senha incorreta. Tente novamente :(")

senha_loop()