def pode_entrar_na_festa():
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            print("Entrada permitida. Bem-vindo(a) à festa!")
        else:
            print("Desculpe, você não pode entrar. Entrada permitida apenas para maiores de 18 anos.")
pode_entrar_na_festa()