def conjunto_frutas():
    frutas = {"Maça", "Banana", "Uva", "Laranja"}
    print("Essas são as frutas do meu conjunto: ")
    for fruta in frutas: 
        print(f"- {fruta}")
conjunto_frutas()

def lista_de_produtos():
    produtos = {
        "notebook": [3500.00, 1000],
        "chinela": 50.00,
        "maçã": 8.50
    }
    
    print("Meus produtos: ")
    for produto in produtos.values():
        print(f"- {produto}")

lista_de_produtos() 
