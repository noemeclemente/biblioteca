import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Criação das tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER,
    conteudo TEXT,
    FOREIGN KEY (autor_id) REFERENCES usuarios(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS feedbacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER,
    usuario_id INTEGER,
    comentario TEXT,
    FOREIGN KEY (livro_id) REFERENCES livros(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
''')

conn.commit()

# Função para cadastrar usuário
def cadastrar_usuario(nome, email):
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()

# Função para escrever um livro
def escrever_livro(titulo, autor_id, conteudo):
    cursor.execute("INSERT INTO livros (titulo, autor_id, conteudo) VALUES (?, ?, ?)", (titulo, autor_id, conteudo))
    conn.commit()

# Função para dar feedback
def dar_feedback(livro_id, usuario_id, comentario):
    cursor.execute("INSERT INTO feedbacks (livro_id, usuario_id, comentario) VALUES (?, ?, ?)", (livro_id, usuario_id, comentario))
    conn.commit()

# Função para listar usuários
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

# Função para listar livros
def listar_livros():
    cursor.execute("SELECT * FROM livros")
    return cursor.fetchall()

# Função para listar feedbacks
def listar_feedbacks():
    cursor.execute("SELECT * FROM feedbacks")
    return cursor.fetchall()

# Exemplos de uso
if __name__ == "__main__":
    # Cadastro de usuários
    cadastrar_usuario('Alice', 'alice@example.com')
    cadastrar_usuario('Bob', 'bob@example.com')

    # Escrever livros
    escrever_livro('O Guia do Mochileiro das Galáxias', 1, 'Um clássico da ficção científica.')
    escrever_livro('1984', 2, 'Uma distopia clássica.')

    # Dar feedback
    dar_feedback(1, 2, 'Adorei esse livro!')
    dar_feedback(2, 1, 'Muito interessante e assustador.')

    # Listar dados
    print("Usuários:", listar_usuarios())
    print("Livros:", listar_livros())
    print("Feedbacks:", listar_feedbacks())

# Fechar a conexão com o banco de dados
conn.close()
