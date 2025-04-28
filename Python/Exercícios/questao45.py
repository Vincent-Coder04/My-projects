tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada.")

def listar_tarefas():
    if tarefas:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Não há tarefas na lista.")

def remover_tarefa():
    tarefa_nome = input("Digite o nome da tarefa a ser removida: ")
    if tarefa_nome in tarefas:
        tarefas.remove(tarefa_nome)
        print(f"Tarefa '{tarefa_nome}' removida.")
    else:
        print(f"Tarefa '{tarefa_nome}' não encontrada.")

def menu():
    while True:
        print("Menu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa (por nome)")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()