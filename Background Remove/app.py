import os 
import re 
import sqlite3 
from flask import Flask, render_template, request, redirect, url_for, session, g 
from werkzeug.utils import secure_filename 

# ---------------------- Configuração Inicial do App ------------------------------------

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'chave_verde' 
app.config['UPLOAD_FOLDER'] = 'static/Images' 

EXTENSOES = {'png', 'jpg', 'jpeg', 'gif'} 

DATABASE = 'users.db' 

# ---------------------- Função para Conectar o Banco ------------------------------------

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row 
    return g.db

@app.teardown_appcontext 
def close_db(error):
    db = g.pop('db', None) 
    if db is not None: 
        db.close()

# ---------------------- Função Auxiliar para Verificar Extensão da Imagem ------------------------------------

def extensao_valida(nome_arquivo):
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1)[1].lower() in EXTENSOES

# ---------------------- Criação das Tabelas (executar uma única vez) ------------------------------------

def inicializar_banco():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   senha TEXT NOT NULL
            );
        ''') 
        db.commit()

# ---------------------- Rota Principal (Index) ------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# ---------------------- Rota Registro de Usuário (register) ------------------------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha2 = request.form['senha2']

        if len(senha) < 8:
            return "Senha fraca. Requisitos: 8+ caracteres, 1 maiuscula, 1 número e 1 símbolo."
        
        if senha != senha2:
            return render_template('register.html', erro="As senhas não coincidem.")
        
        db = get_db()
        try:
            db.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
            db.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Error: CPF ou email já cadastrados."
    return render_template('register.html')

# ---------------------- Rota de Login (login) ------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        usuario = db.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha)).fetchone()
        if usuario:
            session['usuario_id'] = usuario['id']
            session['usuario_nome'] = usuario['nome']
            return redirect(url_for('upload'))
        else:
            return "Login inválido."
    return render_template('login.html')
# ---------------------- Rota para Criar upload I ------------------------------------
@app.route('/upload')
def upload():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    usuario_nome = session.get('usuario_nome')
    mensagem = request.args.get('msg')  
    mensagem2 = request.args.get('msg2') 

    return render_template('upload.html', nome=usuario_nome, mensagem=mensagem, mensagem2=mensagem2)
# ---------------------- Rota para Criar upload II------------------------------------
@app.route('/upload_arquivo', methods=['POST'])
def upload_arquivo():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    arquivo = request.files.get('arquivo')
    if not arquivo or arquivo.filename == '':
        return redirect(url_for('upload', msg='Nenhum arquivo enviado.'))

    nome_arquivo = secure_filename(arquivo.filename)
    caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
    arquivo.save(caminho)
    
    mensagem = f"Arquivo '{nome_arquivo}' salvo com sucesso!"
    mensagem2 = "O arquivo sera mandado sem fundo para o seu Email o mais rápido possível"
    return redirect(url_for('upload', msg=mensagem, msg2=mensagem2))

# ---------------------- Execução Principal ------------------------------------
if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) 
    inicializar_banco()
    app.run(debug=True, host='0.0.0.0', port=5000)

