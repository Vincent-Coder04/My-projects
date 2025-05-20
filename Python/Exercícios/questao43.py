def checar_nome():
    nomes = ["Darth Vader", "Gacha Life", "Palmeiras", "Oshi No Ko", "Ana"]
    nome_usuario = input("Digite um nome: ").strip()

    if nome_usuario in nomes:
        print(f"O nome '{nome_usuario}' está na lista.")
    else:
        print(f"O nome '{nome_usuario}' NÃO está na lista.")

checar_nome()