from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Configurações do banco de dados
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('POSTGRES_DB', 'northwind')
DB_USER = os.getenv('POSTGRES_USER', 'faat')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'faat')

# Função para obter a conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

# Rota para listar todos os alunos
@app.route('/alunos', methods=['GET'])
def obter_alunos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Alunos;')
    alunos = cur.fetchall()
    cur.close()
    conn.close()

    alunos_list = [{"id": aluno[0], "name": aluno[1], "ra": aluno[2]} for aluno in alunos]
    return jsonify(alunos_list)

# Rota para obter um aluno específico
@app.route('/alunos/<int:aluno_id>', methods=['GET'])
def obter_aluno(aluno_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Alunos WHERE aluno_id = %s;', (aluno_id,))
    aluno = cur.fetchone()
    cur.close()
    conn.close()

    if aluno:
        aluno_dict = {"id": aluno[0], "name": aluno[1], "ra": aluno[2]}
        return jsonify(aluno_dict)
    return jsonify({"erro": "Aluno não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')