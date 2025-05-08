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

class AlunoDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Livros (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_aluno(self, nome, titulo, autor):
        self.cursor.execute('''
            INSERT INTO Livros (nome, idade) VALUES (?, ?)
        ''', (nome, titulo, autor))
        self.conexao.commit()
        print(f"Aluno {nome} inserido com sucesso!") 

    def listar_alunos(self):
        self.cursor.execute('SELECT * FROM alunos')
        livros = self.cursor.fetchall()
        print("Lista de alunos: ")
        for livro in livros:
            print(f"ID : {livro[0]} - Nome: {livro[1]} - Idade:{livro[2]}")

def menu():
    dao = AlunoDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir Livro")
        print("2 - Listar Livros")
        print("3 - Sair")
        opcao = input("Escolha uma opção:")
        if opcao =="1":
         try:
            nome = input("Digite o nome do Livro: ")
            titulo = input("Digite o nome do titulo do livro: ")
            autor = input("Digite o nome do autor: ")

            dao.inserir_aluno()
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