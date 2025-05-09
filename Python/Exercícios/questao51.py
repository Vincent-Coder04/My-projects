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
'''
Exercício 3 : Inserção de Professores
Descrição:
Crie uma classe ProfessorDAO para:
 Criar a tabela professores com os campos id, nome, disciplina
 Receber pelo menos 2 cadastros via input
 Exibir todos os professores com print(f&quot;{nome} ministra {disciplina}&quot;)
'''
'''
Exercício 4 : Cadastro de Clientes
Descrição:
Implemente uma classe ClienteDAO com os métodos:
 criar_tabela() com os campos: id, nome, email
 inserir_cliente() via input
 listar_clientes() exibindo todos com formatação clara
'''
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
'''
'''
Exercício 6 : Identifique o erro
Descrição:
Veja o código abaixo e diga por que ele falha:
self.cursor.execute(&quot;INSERT INTO alunos (nome, idade) VALUES (?, ?)&quot;,
&quot;Carlos&quot;, 18)
Pergunta:
O que precisa ser corrigido nessa linha para que o comando funcione
'''