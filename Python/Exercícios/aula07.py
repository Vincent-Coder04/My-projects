def solicitar_idade():
    while True: 
        idade = int(input("Digite sua idade:"))

        if idade >= 0 and idade <=120: 
            print("Idade registrada: ", idade) 
            break 
        else:
            print("Idade Inválida. Tente novamente!")

solicitar_idade() 
