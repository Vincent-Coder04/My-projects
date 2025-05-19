import os 
import sqlite3 
from flask import Flask, render_template, request, redirect, url_for

# Configurações Inicias
app = Flask(__name__) # Serve para inicializar a nossa aplicação
DATABASE = 'tasks.db' # Definir o nome do nosso banco

# Função para conectar o banco de dados
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Criação das tabelas de banco de dados
def inicializar_banco():
    with get_db() as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS tarefas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   descricao TEXT NOT NULL
                );
            ''')
        
# Rotas da aplicação (detalhe: só tem index aqui LMAO)
@app.route('/')
def index():
    db = get_db()
    tarefas = db.execute('SELECT * FROM tarefas').fetchall()
    return render_template('index.html', tarefas = tarefas)

@app.route('/add', methods=['POST'])
def add():
    descricao = request.form['descricao']
    if descricao:
        db = get_db()
        db.execute('INSERT INTO tarefas (descricao) VALUES (?)', (descricao,))
        db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    db = get_db()
    db.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))

# Execução do app

if __name__ == '__main__':
    inicializar_banco()
    app.run(debug=True)
