import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'seu_segredo_aqui'

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)",
                           (nome, email, senha_hash))
            conn.commit()
            conn.close()
            flash('Usuário registrado com sucesso!')
            return redirect(url_for('register'))
        except sqlite3.IntegrityError:
            flash('Este e-mail já está cadastrado.')
            return redirect(url_for('register'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

