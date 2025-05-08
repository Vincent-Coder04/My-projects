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


def menu():
    dao = AlunoDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir aluno")
        print("2 - Listar alunos")
        print("3 - Sair")
        opcao = input("Escolha uma opção:")
        if opcao =="1":
         try:
            nome = input("Digite o nome do aluno: ")
            
            idade = int(input("Digite a idade do aluno: "))
            dao.inserir_aluno(nome, idade)
         except ValueError:
           print("Digite um valor válido")
           continue
        elif opcao == "2":
            dao.listar_alunos()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando...")
            break
        else:
            print("Digite um valor entre 1 a 3\n")
            
menu()
