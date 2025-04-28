def conjuntos():
    global cursos_manha 
    global cursos_noite
    cursos_manha = set(["curso do amostradinho", "curso do casca de bala", "curso do lá ele", "curso do chikcen jockey"])
    cursos_noite = set(["curso do fliench stell", "curso do THE NETHER", "curso do I'M STEVE", "curso do RELEASE", "curso do lá ele"])

def cursodia():
    print("Cursos ofertados no período da manhã:")
    for curso in cursos_manha:
        print(curso)

def cursonoite():
    print("Cursos ofertados no período da noite:")
    for curso in cursos_noite:
        print(curso)

def intersecao_conjuntos():
    cursos_comum = cursos_manha & cursos_noite
    print("Cursos ofertados tanto na manhã quanto na noite:")
    if cursos_comum:
        for curso in cursos_comum:
            print(curso)
    else:
        print("Não há cursos comuns nos dois períodos.")

def menu():
    conjuntos()

    while True:
        print("\nMenu:")
        print("1. Cursos ofertados no período da manhã.")
        print("2. Cursos ofertados no período da noite.")
        print("3. Cursos ofertados na manhã e noite.")
        print("4. Sair.")

        try:
            opcao = int(input("Digite um valor entre 1-4: "))
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 4.")
            continue  

        if opcao == 1:
            cursodia()
        elif opcao == 2:
            cursonoite()
        elif opcao == 3:
            intersecao_conjuntos()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 4.")

menu()