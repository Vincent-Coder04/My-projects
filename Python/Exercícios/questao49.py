def southamerica():
    global paises 
    paises = set(["Peru", "Brazil", "Ecuador", "Suriname", "Guyana", "Venezuela", "Chile", "Argentina", "Colomia", "Uruguay", "Paraguay"])

def sussypussy():
    for i in range(3):
        pais = input(f"Digite o nome do {i+1}º país: ").strip().capitalize()
        if pais in paises:
            print(f"{pais} está presente no conjunto.")
        else:
            print(f"{pais} não está presente no conjunto.")
    
southamerica()
sussypussy()
