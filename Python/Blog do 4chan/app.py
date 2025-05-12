import os # Biblioteca para lidar com arquivos e diretórios
import re # Biblioteca para validações com expressões regulares (senha)
import sqlite3 # Biblioteca padrão do python para bancos de dados SQLite
from flask import Flask, render_template, request, redirect, url_for, session, g
from werkzeug.utils import secure_filename # Biblioteca que garante nomes seguros para arquivos enviados 

# - - - - - - - - - - - - - - - Configuração Inicial do App - - - - - - - - - - - - - - - - - - - - - - - - - - - -

app = Flask(__name__) # Criação da aplicação flask
app.config['SECRET_KEY'] = 'chave_mauri' # Chave secreta utilizada nas sess~
app.config['UPLOAD_FOLDER'] = 'static/uploads' # Pasta para onde imagens serão salvas
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 ** 1024 # Limite do tamanho de upload para 2mb

EXTENSOES = {'png', 'jpg', 'jpeg', 'gif'}

DATABASE = 'meublog.db' # Nome do banco SQLite

# - - - - - - - - - - - - - - - Função para Conectar o Banco - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_db():
    # Estabelecer e retornar a conexão com o banco de dados SQLite.
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row # Permite acessar os dados como dicionários (ex: linha['email'])
    return g.db 

@app.teardown_appcontext # Automatiza a execução após cada requisição por conta desse decorador
def close_db(error):
    # Fechar a conexão com o banco após cada requisição
    # Esse 'g' é um objeto especial do Flask usado para armazenar dados globais da aplicação durante uma requisição (como variáveis que você quer acessar em vários lugares durante uma requisição HTTP).
    db = g.pop('db', None) # Remove a conexão com o banco de g e armazena em db. Se não existir, retorna None.
    if db is not None: # Se havia uma conexão, ela é fechada
        db.close()

# - - - - - - - - - - - - - - - Função Auxiliar para Verificar Extensão da Imagem- - - - - - - - - - - - - - - - - - - - - - - - - - - -

def extensao_valida(nome_arquivo):
    # Verificar se a extensão do arquivo enviado é uma das permitidas
    # Verificar se o nome do arquivo posui um ponto
    # 'nome_arquivp.rsplit('.', 1): separa o nome do arquivo da extensão, da direita para a esquerda, uma vez só'
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1).lower in EXTENSOES

# - - - - - - - - - - - - - - - Criação das tabelas (executar uma única vez) - - - - - - - - - - - - - - - - - - - - - - - - - - -

def inicializar_banco():
    # Criar as tabelas do banco caso não existam
    with app.app_context():
        db = get_db() 
        db.execute('''
            CREATE TABLE IF NOT EXIST usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT UNIQUE,
                    email TEXT UNIQUE NOT NULL, 
                    senha TEXT NOT NULL
            );
        ''')
        db.execute('''
             CREATE TABLE IF NOT EXIST posts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    título TEXT NOT NULL,
                    conteudo TEXT NOT NULL,
                    imagem TEXT,
                    autor_id INTEGER NOT NULL,
                    FOREING KEY(autor_id) REFERENCES usuarios (id)
                  );
              ''')
        db.commit()
# - - - - - - - - - - - - - - - Rota Principal (index) - - - - - - - - - - - - - - - - - - - - - - - - - - -

@app.route('/')
def index():
    # Exibir todos os posts públicos na página inicial
    db = get_db()
    posts = db.execute('''
       SELECT p.título, p.conteudo, p.imagem, u.nome 
       FROM posts p
       JOIN usuario u on p.autor_id = i.id
       ''')
# - - - - - - - - - - - - - - - Rota Registro de Usuário (register) - - - - - - - - - - - - - - - - - - - - - - - - - - -

@app.route('/register', methods=['GET', 'POST'])


