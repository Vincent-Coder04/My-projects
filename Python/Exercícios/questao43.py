def skibiditoalete():
    lista = ["Ana", "Pedro", "Darth Vader", "Palmeiras", "Gacha Life"]
    
    while True:
        nome = input("Digite um nome aqui e veja se ele está na lista ou Digite 'sair' para encerrar: ")
        
        if nome == "sair":
            print("Você escolheu sair. Encerrando o programa.")
            break
        elif nome in lista:
            print(f"'{nome}' está na lista!")
            break
        else:
            print(f"'{nome}' não está na lista. Tente novamente!")

skibiditoalete()