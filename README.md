# Sistema de Gerenciamento de Biblioteca

Este projeto é uma aplicação simples de gerenciamento de biblioteca utilizando SQLite como banco de dados. O sistema permite a criação de tabelas para usuários, livros e feedbacks, além de fornecer funções para cadastrar usuários, escrever livros e adicionar feedbacks.

## Funcionalidades

- **Cadastro de Usuários**: Adiciona novos usuários ao banco de dados.
- **Cadastro de Livros**: Adiciona novos livros com o ID do autor.
- **Adição de Feedbacks**: Adiciona comentários sobre livros por usuários.
- **Listagem de Dados**: Lista usuários, livros e feedbacks armazenados no banco de dados.

## Estrutura do Código

### Banco de Dados

O banco de dados SQLite é criado com as seguintes tabelas:

- **`usuarios`**: Armazena informações sobre os usuários.
  - `id`: Identificador único do usuário (chave primária).
  - `nome`: Nome do usuário.
  - `email`: E-mail do usuário (único).

- **`livros`**: Armazena informações sobre os livros.
  - `id`: Identificador único do livro (chave primária).
  - `titulo`: Título do livro.
  - `autor_id`: ID do autor (referência para a tabela `usuarios`).
  - `conteudo`: Descrição ou conteúdo do livro.

- **`feedbacks`**: Armazena feedbacks sobre os livros.
  - `id`: Identificador único do feedback (chave primária).
  - `livro_id`: ID do livro (referência para a tabela `livros`).
  - `usuario_id`: ID do usuário (referência para a tabela `usuarios`).
  - `comentario`: Comentário do usuário sobre o livro.

### Funções Principais

- **`cadastrar_usuario(nome, email)`**: Adiciona um novo usuário à tabela `usuarios`.
- **`escrever_livro(titulo, autor_id, conteudo)`**: Adiciona um novo livro à tabela `livros`.
- **`dar_feedback(livro_id, usuario_id, comentario)`**: Adiciona um feedback à tabela `feedbacks`.
- **`listar_usuarios()`**: Lista todos os usuários cadastrados.
- **`listar_livros()`**: Lista todos os livros cadastrados.
- **`listar_feedbacks()`**: Lista todos os feedbacks cadastrados.

### Exemplos de Uso

No bloco de código principal, são realizados os seguintes passos:

1. Cadastro de usuários:
   ```python
   cadastrar_usuario('Alice', 'alice@example.com')
   cadastrar_usuario('Bob', 'bob@example.com')
2. Cadastro de livros:
```
escrever_livro('O Guia do Mochileiro das Galáxias', 1, 'Um clássico da ficção científica.')
escrever_livro('1984', 2, 'Uma distopia clássica.')
```
3. Adição de feedbacks:
```
dar_feedback(1, 2, 'Adorei esse livro!')
dar_feedback(2, 1, 'Muito interessante e assustador.')
```
4. Listagem de dados:
```
print("Usuários:", listar_usuarios())
print("Livros:", listar_livros())
print("Feedbacks:", listar_feedbacks())
```
# Requisitos 
- Python
- sqlite3: incluído na biblioteca padrão do python
  
# Como executar
```
python seu_arquivo.py
```
# Contribuições
Sinta-se à vontade para contribuir com melhorias ou correções. Abra uma issue ou envie um pull request.
