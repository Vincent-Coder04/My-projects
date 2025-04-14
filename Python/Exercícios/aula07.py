def solicitar_idade():
    while True: #Início do loop condicional - enquanto for verdade
        idade = int(input("Digite sua idade:"))

        if idade >= 0 and idade <=120: # Condição de repetição
            print("Idade registrada: ", idade) 
            break # Estrutura que indica condição de parada
        else:
            print("Idade Inválida. Tente novamente!")

solicitar_idade() # Chamada da função
