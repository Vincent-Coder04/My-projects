'''
Exercício 1 : Cadastro de Livros
Descrição:
Crie uma classe LivroDAO que:
 Crie uma tabela livros com os campos: id, titulo e autor
 Permita inserir livros com título e autor
 Liste todos os livros cadastrados no banco
'''
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="Livros.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class LivroDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_livro(self, titulo, autor):
        self.cursor.execute('''
            INSERT INTO Livros (titulo, autor) VALUES (?, ?)
        ''', (titulo, autor))
        self.conexao.commit()
        print(f"Livro '{titulo}' de {autor} inserido com sucesso!") 

    def listar_livros(self):
        self.cursor.execute('SELECT * FROM Livros')
        livros = self.cursor.fetchall()
        if not livros:
            print("Nenhum livro cadastrado.")
            return
        print("Lista de livros:")
        for livro in livros:
            print(f"ID: {livro[0]} - Título: {livro[1]} - Autor: {livro[2]}")

    def limpar_tabela(self):
        self.cursor.execute('DELETE FROM Livros')
        self.cursor.execute('DELETE FROM sqlite_sequence WHERE name="Livros"') 
        self.conexao.commit()
        print("Todos os livros foram apagados.")

def menu():
    dao = LivroDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir Livro")
        print("2 - Listar Livros")
        print("3 - Sair")
        print("4 - Apagar todos os livros")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            dao.inserir_livro(titulo, autor)
        elif opcao == "2":
            dao.listar_livros()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando...")
            break
        elif opcao == "4":
            confirmar = input("Tem certeza que quer apagar todos os livros? (s/n): ")
            if confirmar.lower() == "s":
                dao.limpar_tabela()
            else:
                print("Ação cancelada.")
        else:
            print("Digite um valor entre 1 a 4.\n")

menu()
'''
Exercício 2 : Cadastro de Cursos com Nível
Descrição:
Implemente uma classe CursoDAO que:
 Crie a tabela cursos com: id, nome, nivel (iniciante, intermediário,
avançado)
 Insira 3 cursos diferentes
 Liste todos os cursos disponíveis
'''
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="Cursos.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class CursosDAO(ConexaoBanco):
    def criar_tabelas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CursosIniciantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CursosIntermediarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CursosAvancados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_curso(self, nome, tabela):
        self.cursor.execute(f'''
            INSERT INTO {tabela} (nome) VALUES (?)
        ''', (nome,))
        self.conexao.commit()
        print(f"Curso '{nome}' adicionado com sucesso à tabela {tabela}.")

    def listar_cursos(self, tabela):
        self.cursor.execute(f'SELECT * FROM {tabela}')
        cursos = self.cursor.fetchall()
        if not cursos:
            print(f"Nenhum curso encontrado na tabela {tabela}.")
        else:
            print(f"Cursos na tabela {tabela}:")
            for curso in cursos:
                print(f"ID: {curso[0]} - Nome: {curso[1]}")

    def limpar_tabela(self, tabela):
        self.cursor.execute(f'DELETE FROM {tabela}')
        self.cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{tabela}"')
        self.conexao.commit()
        print(f"Todos os cursos foram apagados da tabela {tabela}.")

def menu():
    dao = CursosDAO()
    dao.criar_tabelas()

    while True:
        print("--- MENU ---")
        print("1 - Inserir Curso Nível Iniciante")
        print("2 - Inserir Curso Nível Intermediário")
        print("3 - Inserir Curso Nível Avançado")
        print("4 - Listar Todos os cursos")
        print("5 - Limpar Todas as tabelas")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do curso iniciante: ")
            dao.inserir_curso(nome, "CursosIniciantes")
        elif opcao == "2":
            nome = input("Digite o nome do curso intermediário: ")
            dao.inserir_curso(nome, "CursosIntermediarios")
        elif opcao == "3":
            nome = input("Digite o nome do curso avançado: ")
            dao.inserir_curso(nome, "CursosAvancados")
        elif opcao == "4":
            dao.listar_cursos("CursosIniciantes")
            dao.listar_cursos("CursosIntermediarios")
            dao.listar_cursos("CursosAvancados")
        elif opcao == "5":
             tabelas = ["CursosIniciantes", "CursosIntermediarios", "CursosAvancados"]
             for tabela in tabelas:
                dao.limpar_tabela(tabela)
        elif opcao == "6":
            dao.fechar()
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 6.")
menu()

'''
Exercício 3 : Inserção de Professores
Descrição:
Crie uma classe ProfessorDAO para:
 Criar a tabela professores com os campos id, nome, disciplina
 Receber pelo menos 2 cadastros via input
 Exibir todos os professores com print(f&quot;{nome} ministra {disciplina}&quot;)
'''
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="Professores.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()

class ProfessoresDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Professores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                disciplina TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_professores(self, nome, disciplina):
        self.cursor.execute('''
            INSERT INTO Professores (nome, disciplina) VALUES (?, ?)
        ''', (nome, disciplina))
        self.conexao.commit()
        print(f"Professor/a '{nome}' da disciplina '{disciplina}' inserido/a com sucesso!") 

    def listar_professores(self):
        self.cursor.execute('SELECT * FROM Professores')
        Professores = self.cursor.fetchall()
        if not Professores:
            print("Nenhum livro cadastrado.")
            return
        print("Lista de Professores e Disciplinas:")
        for Professor in Professores:
            print(f"ID: {Professor[0]} - Nome: {Professor[1]} - Disciplina: {Professor[2]}")

    def limpar_tabela(self):
        self.cursor.execute('DELETE FROM Professores')
        self.cursor.execute('DELETE FROM sqlite_sequence WHERE name="Professores"') 
        self.conexao.commit()
        print("Todos os Professores foram Mortos.")

def menu():
    dao = ProfessoresDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir Professor/a")
        print("2 - Listar Professores")
        print("3 - Sair")
        print("4 - Apagar todos os Professores da existência")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do Professor: ")
            disciplina = input("Digite o nome da disciplina: ")
            dao.inserir_professores(nome, disciplina)
        elif opcao == "2":
            dao.listar_professores()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando...")
            break
        elif opcao == "4":
            confirmar = input("Tem certeza que quer apagar todos os Professoras da existência? (s/n): ")
            if confirmar.lower() == "s":
                dao.limpar_tabela()
            else:
                print("Ação cancelada.")
        else:
            print("Digite um valor entre 1 a 4.\n")

menu()
'''
Exercício 4 : Cadastro de Clientes
Descrição:
Implemente uma classe ClienteDAO com os métodos:
 criar_tabela() com os campos: id, nome, email
 inserir_cliente() via input
 listar_clientes() exibindo todos com formatação clara
'''
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="Clientes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()

class ClientesDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_clientes(self, nome, email):
        self.cursor.execute('''
            INSERT INTO Clientes (nome, email) VALUES (?, ?)
        ''', (nome, email))
        self.conexao.commit()
        print(f"Cliente {nome}, com email {email} adicionado com sucesso!") 

    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM Clientes')
        clientes = self.cursor.fetchall()
        if not clientes:
            print("Nenhum Cliente cadastrado.")
            return
        print("Lista de Clientes :")
        for cliente in clientes:
            print(f"ID: {cliente[0]} - Nome: {cliente[1]} - Email: {cliente[2]}")

    def limpar_tabela(self):
        self.cursor.execute('DELETE FROM Clientes')
        self.cursor.execute('DELETE FROM sqlite_sequence WHERE name="Clientes"') 
        self.conexao.commit()
        print("Todos os Clientes foram Mortos.")

def menu():
    dao = ClientesDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Sair")
        print("4 - Apagar todos os Clientes da existência")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do Cliente: ")
            email = input("Digite o Email: ")
            dao.inserir_clientes(nome, email)
        elif opcao == "2":
            dao.listar_clientes()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando...")
            break
        elif opcao == "4":
            confirmar = input("Tem certeza que quer apagar todos os Clientes da existência? (s/n): ")
            if confirmar.lower() == "s":
                dao.limpar_tabela()
            else:
                print("Ação cancelada.")
        else:
            print("Digite um valor entre 1 a 4.\n")

menu()
'''
Exercício 5 : Análise de Código (Criação de Tabela)
Descrição:
Analise o trecho de código abaixo:

class AnimalDAO:
def criar_tabela(self):
self.cursor.execute(&#39;&#39;&#39;
CREATE TABLE animais (
nome TEXT,
especie TEXT
)
&#39;&#39;&#39;)
Pergunta:
Quais dois erros ou problemas você consegue identificar nesse código?
(Dica: pense na estrutura da tabela e na classe)
R:A classe AnimalDAO não está vinculada a nenhuma classe que tem as propriedades de bancos de dados, como ConexaoBanco, não tem o IF NOT EXIST que é importante para garantir uma tabela segura e evite erros.
'''
'''
Exercício 6 : Identifique o erro
Descrição:
Veja o código abaixo e diga por que ele falha: Ele falha porque não usa a estrutura adequada para que o INSERT funcione
Pergunta:
O que precisa ser corrigido nessa linha para que o comando funcione: Não deu :(
'''
