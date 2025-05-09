import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="alunos.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class AlunoDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_aluno(self, nome, idade):
        self.cursor.execute('''
            INSERT INTO alunos (nome, idade) VALUES (?, ?)
        ''', (nome, idade))
        self.conexao.commit()
        print(f"Aluno {nome} inserido com sucesso!") 

    def listar_alunos(self):
        self.cursor.execute('SELECT * FROM alunos')
        alunos = self.cursor.fetchall()
        print("Lista de alunos: ")
        for aluno in alunos:
            print(f"ID : {aluno[0]} - Nome: {aluno[1]} - Idade:{aluno[2]}")
    
    def buscar_por_nome(self, nome):
        self.cursor.execute('SELECT * FROM alunos WHERE nome = ?', (nome,))
        resultado = self.cursor.fetchall()
        if resultado:
            for aluno in resultado:
                print(f"Encontrado: ID {aluno[0]} - Nome {aluno[1]} - Idade {aluno[2]}")
        else:
            print("Aluno não encontrado")

    def atualizar_idade(self, nome, nova_idade):
        self.cursor.execute('UPDATE alunos SET idade = ? WHERE id = ?', (nova_idade, nome))
        self.conexao.commit()
        print(f"Idade de {nome} foi atualizada para {nova_idade}")

    def deletar_aluno(self, nome):
        self.cursor.execute('DELETE FROM alunos WHERE nome = ?', (nome,))
        self.conexao.commit()
        print(f"Aluno {nome} foi removido com sucesso")

def menu():
    dao = AlunoDAO()
    dao.criar_tabela()

    while True:
        print("\n1 - Inserir aluno")
        print("2 - Listar alunos")
        print("3 - Buscar por nome")
        print("4 - Atualizar idade")
        print("5 - Deletar aluno")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nome = input("Digite o id do aluno: ")
                idade = int(input("Digite a idade do aluno: "))
                dao.inserir_aluno(nome, idade)
            except ValueError:
                print("Digite uma idade válida.")
        elif opcao == "2":
            dao.listar_alunos()
        elif opcao == "3":
            nome = input("Digite o nome para buscar: ")
            dao.buscar_por_nome(nome)
        elif opcao == "4":
            nome = input("Digite o nome do aluno: ")
            try:
                nova_idade = int(input("Digite a nova idade: "))
                dao.atualizar_idade(nome, nova_idade)
            except ValueError:
                print("Digite uma idade válida.")
        elif opcao == "5":
            nome = input("Digite o nome do aluno para deletar: ")
            dao.deletar_aluno(nome)
        elif opcao == "6":
            dao.fechar()
            print("Encerrando...")
            break
        else:
            print("Digite um valor entre 1 e 6.")

menu()