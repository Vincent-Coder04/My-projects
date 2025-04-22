def cadastrar_alunos():
    alunos = []  
    
    while True:  
        nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ")
        
        if nome.lower() == "sair":  
            break 
    
        alunos.append(nome) 

    print("Alunos cadastrados:")
    for aluno in alunos:
        print(aluno)
    
    print(f"Quantidade de alunos cadastrados: {len(alunos)}")

cadastrar_alunos()