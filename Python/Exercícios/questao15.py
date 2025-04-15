def nome_com_a():
    for i in range(5):
        nome= input("Digite o nome: ")
        if nome.lower().startswith("a"):
            print(f"O nome {nome} começa com a letra A")
            

nome_com_a()