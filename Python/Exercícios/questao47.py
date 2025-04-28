def conjuntos():
    global cursos_manha 
    global cursos_noite
    cursos_manha = set(["curso do amostradinho", "curso do casca de bala", "curso do lá ele", "curso do chikcen jockey"])
    cursos_noite = set(["curso do fliench stell", "curso do THE NETHER", "curso do I'M STEVE", "curso do RELEASE", "curso do lá ele"])

def cursodia():
    print(f"{cursos_manha}")

def cursonoite():
    print(f"{cursos_noite}")

def intersecao_conjuntos(cursos_manha, cursos_noite):
    cursos_comum = intersecao_conjuntos(cursos_manha, cursos_noite)
    print(f"{cursos_comum}")

def menu():
    while True:
        print("Menu:")
        print("1. Cursos ofertados no período da manhã.")
        print("2. Cursos ofertados no período da noite.")
        print("3. Cursos ofertados na manhã e noite. ")
        print("4. Sair. ")

        opcao = int(input("Digite um valor entre 1-4: "))
        if opcao == "1":
                cursodia()
        elif opcao == "2":
                cursonoite()
        elif opcao == "3":
                intersecao_conjuntos()
        elif opcao == "4":
              print("Saindo...")
              break
menu()
    



