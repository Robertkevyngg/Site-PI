from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="site"
)

cursor = db.cursor()

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar um usuário
@app.route('/add_user', methods=['POST'])
def add_user():
    nome = request.form['nome']
    email = request.form['email']

    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome, email)
    cursor.execute(sql, valores)
    db.commit()

    return "Usuário adicionado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
