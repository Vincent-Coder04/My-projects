def pode_entrar_na_festa():
    try:
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            print("Entrada permitida. Bem-vindo(a) à festa!")
        else:
            print("Desculpe, você não pode entrar. Entrada permitida apenas para maiores de 18 anos.")
    except ValueError:
        print("Por favor, digite um número válido para a idade.")

pode_entrar_na_festa()