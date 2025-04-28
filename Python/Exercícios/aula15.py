def produtos_com_mais_coisas():
    produtos = {
        "Notebook" : ("LG", 3500, "Cartão em até 12x com acréscimo"),
        "Monitor" : ("Samsung", 1400.00, "Cartão em 6x sem juros"),
        "Teclado" : ("Logitec", 122.00, "Á vista")
    }

    print("Produtos Cadastrados: ")
    for produto, detalhes, in produtos.items():
        marca, preco, pagamento = detalhes 
        print(f"Produto: {produto}")
        print(f"- Marca: {marca}")
        print(f"- Preço: {preco:.2f}")
        print(f"- Pagamento:{pagamento}\n")
    
produtos_com_mais_coisas()
