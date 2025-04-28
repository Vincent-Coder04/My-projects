def cities():
    cidades = set()  

    for i in range(8):
        digitar = input(f"Digite o nome da {i+1}ª cidade: ")
        cidades.add(digitar)
    
    print("Cidades digitadas:")
    for index, cidade in enumerate(sorted(cidades), start=1):
        print(f"{index}. {cidade}") 
    print(cidades)
cities()