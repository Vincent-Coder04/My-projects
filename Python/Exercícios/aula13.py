def cadastrar_produtos():
    produtos =[] 
    while True:
        produto = input("Digite o nome do produto ou digite sair para encerrar: ")
        if produto.lower() == "Sair": 
            break
        produtos.append(produto)

    print("Produto cadastrados>: ")
    print(produtos)

cadastrar_produtos()
