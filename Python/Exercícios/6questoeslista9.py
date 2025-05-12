'''
1. [Sistema da Cantina Escolar : Cadastro de Lanches]
Contexto: A cantina da escola quer organizar os lanches disponíveis no dia. Eles
precisam de uma base de dados simples com nome do lanche e seu preço.
Desafio:
Crie uma classe LancheDAO com métodos para:
 Criar a tabela lanches
 Inserir ao menos 3 lanches
 Listar todos os lanches disponíveis na cantina
'''
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="Lanches.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    def fechar(self):
        self.conexao.close()

class LanchesDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Lanches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lanche NOT NULL, 
                preco NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_lanches(self, lanche, preco):
        try:
            self.cursor.execute('''
                INSERT INTO Lanches (lanche, preco) VALUES (?, ?)
            ''', (lanche, preco))
            self.conexao.commit()
            print(f"Lanche '{lanche}' com preço R${preco:.2f} foi adicionado com sucesso!") 
        except sqlite3.IntegrityError:
            print(f"Erro: o lanche '{lanche}' já existe.")

    def listar_lanches(self):
        self.cursor.execute('SELECT * FROM Lanches')
        lanches = self.cursor.fetchall()
        if not lanches:
            print("Nenhum Lanche cadastrado.")
            return
        print("Lista de Lanches:")
        for lanche in lanches:
            print(f"Lanche: {lanche[0]} - Preço: R${lanche[1]:.2f}")

    def limpar_tabela(self):
        self.cursor.execute('DELETE FROM Lanches')
        self.conexao.commit()
        print("Todos os Lanches foram removidos.")

def menu():
    dao = LanchesDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir Lanches")
        print("2 - Listar Lanches")
        print("3 - Sair")
        print("4 - Apagar todos os Lanches da existência")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lanche = input("Digite o nome do Lanche: ")
            preco = float(input("Digite o preço do lanche: "))
            dao.inserir_lanches(lanche, preco)
        elif opcao == "2":
            dao.listar_lanches()
        elif opcao == "3":
            dao.fechar()
            print("Encerrando...")
            break
        elif opcao == "4":
            confirmar = input("Tem certeza que quer apagar todos os Lanches da existência? (s/n): ")
            if confirmar.lower() == "s":
                dao.limpar_tabela()
            else:
                print("Ação cancelada.")
        else:
            print("Digite um valor entre 1 a 4.")

menu()
'''
2. [Estação Gamer : Atualizando o Preço do PC]
Contexto: Um aluno está montando uma loja fictícia de informática para atender
gamers. Ele cadastrou seus produtos, mas percebeu que o preço da placa de vídeo estava
errado.
Desafio:
Implemente um método atualizar_preco() dentro da classe ProdutoDAO que:
 Atualize o preço de um produto específico (informado pelo nome)
 Após a atualização, exiba a lista atualizada dos produtos
'''
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="Produtos.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class ProdutosDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa_de_video TEXT NOT NULL,
                preco REAL NOT NULL
            )
        ''')
        self.conexao.commit()

    def inserir_placa_de_video(self, placa_de_video, preco):
        self.cursor.execute('''
            INSERT INTO Produtos (placa_de_video, preco) VALUES (?, ?)
        ''', (placa_de_video, preco))
        self.conexao.commit()
        print(f"Placa de vídeo '{placa_de_video}' com preço de R${preco:.2f} adicionada com sucesso!") 

    def listar_placas_de_videos(self):
        self.cursor.execute('SELECT placa_de_video, preco FROM Produtos')
        produtos = self.cursor.fetchall()
        if not produtos:
            print("Nenhuma placa de vídeo cadastrada.")
            return
        print("Lista de placas de vídeo:")
        for produto in produtos:
            print(f"Placa de Vídeo: {produto[0]} - Preço: R${produto[1]:.2f}")

    def atualizar_preco(self, placa_de_video, novo_preco):
        self.cursor.execute('''
            UPDATE Produtos SET preco = ? WHERE placa_de_video = ?
        ''', (novo_preco, placa_de_video))
        self.conexao.commit()
        print(f"Preço da placa '{placa_de_video}' atualizado para R${novo_preco:.2f}")

def menu():
    dao = ProdutosDAO()
    dao.criar_tabela()

    while True:
        print("\n1 - Inserir Placa de vídeo")
        print("2 - Listar Placas de vídeos")
        print("3 - Atualizar Preço")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Digite o nome da Placa de vídeo: ")
            try:
                preco = float(input("Digite o Preço da placa de vídeo: "))
                dao.inserir_placa_de_video(placa, preco)
            except ValueError:
                print("Preço inválido. Use apenas números.")
        elif opcao == "2":
            dao.listar_placas_de_videos()
        elif opcao == "3":
            placa = input("Digite o nome da placa: ")
            try:
                novo_preco = float(input("Digite o novo preço: "))
                dao.atualizar_preco(placa, novo_preco)
            except ValueError:
                print("Preço inválido.")
        elif opcao == "4":
            dao.fechar()
            print("Encerrando...\n")
            break
        else:
            print("Digite um valor entre 1 e 4.")

menu()
'''
3. [Controle de Visitantes : Removendo os que já saíram]
Contexto: A escola está testando um sistema de controle de entrada e saída de
visitantes. Cada visitante é registrado com nome e o motivo da visita. Quando ele vai
embora, o cadastro precisa ser removido.
Desafio:
Crie uma classe VisitanteDAO com:
 Criação da tabela visitantes
 Inserção de visitantes
 Método remover_visitante(nome) que deleta um visitante pelo nome
 Listagem dos visitantes ainda presentes
'''
import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="Visitantes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class VisitantesDAO(ConexaoBanco):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Visitantes (
                nome TEXT
            )
        ''')
        self.conexao.commit()

    def inserir_visitante(self, nome):
        self.cursor.execute('''
            INSERT INTO Visitantes (nome) VALUES (?)
        ''', (nome))
        self.conexao.commit()
        print(f"Visitante {nome} inserido com sucesso!") 

    def listar_visitantes(self):
        self.cursor.execute('SELECT * FROM Visitantes')
        visitantes = self.cursor.fetchall()
        print("Lista de visitantes: ")
        for visitante in visitantes:
            print(f"Nome : {visitante[0]}")
        if not visitantes:
            print("Nenhuma Visitante cadastrado.")
            return
    
    def deletar_visitante(self, nome):
        self.cursor.execute('DELETE FROM Visitantes WHERE nome = ?', (nome,))
        self.conexao.commit()
        print(f"Visitante {nome} foi removido com sucesso")

def menu():
    dao = VisitantesDAO()
    dao.criar_tabela()

    while True:
        print("1 - Inserir Visitante")
        print("2 - Listar Visitantes")
        print("3 - Deletar Visitante")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
                nome = input("Digite o nome do visitante: ")
                dao.inserir_visitante(nome)
        elif opcao == "2":
            dao.listar_visitantes()
        elif opcao == "3":
            nome = input("Digite o nome do visitante para deletar: ")
            dao.deletar_visitante(nome)
        elif opcao == "4":
            dao.fechar()
            print("Encerrando...")
            break
        else:
            print("Digite um valor entre 1 e 4.")

menu()
'''
4. [Clube de Leitura : Buscar Livro pelo Título]
Contexto: O Clube de Leitura do SENAC tem uma base com livros e autores. Os
alunos querem poder buscar um livro específico pelo nome e ver o autor
correspondente.
Desafio:
Crie uma classe LivroDAO com:
 Criação da tabela livros (campos: id, titulo, autor)
 Inserção de livros via input
 Método buscar_por_titulo(titulo) para buscar e exibir um livro específico
'''
'''
5. [Loja de Camisetas : Atualizando o Estoque]
Contexto: A loja fictícia &quot;CodeWear&quot; quer manter o controle de estoque das camisetas.
Quando uma camiseta é vendida, a quantidade disponível deve ser atualizada no banco.
Desafio:
Monte a tabela camisetas com:
 nome do modelo
 cor
 quantidade
Depois, implemente:
 Inserção de pelo menos 2 camisetas
 Método atualizar_quantidade(modelo, nova_qtd)
 Método de listagem geral
'''
'''
6. [Ranking de Alunos no Campeonato de Xadrez]
Contexto: Após um campeonato de xadrez interno, os alunos querem registrar os
nomes e pontuações no banco de dados.
Desafio:
Crie a tabela ranking com nome e pontuação.
Implemente:
 Inserção dos alunos
 Método buscar_por_pontuacao(min_pontuacao) para listar todos os alunos
com pontuação igual ou superior ao valor informado.
'''