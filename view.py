import sqlite3

# Conectar ao banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn)\
                VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()    
    conn.close()


# Função para inserir usuários    
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                VALUES(?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, telefone))

# funcao para exibir os livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * from livros").fetchall()
    conn.close()

    if not livros:
        print("Nenhum livro encontrado na biblioteca.")
        return 
    
    print("Livros na biblioteca: ")
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"titulo: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Editora: {livro[3]}")
        print(f"Ano de publicacao: {livro[4]}")
        print(f"ISBN: {livro[5]}")
        print("\n")

# Função para realizar empréstimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()        
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                 VALUES(?, ?, ?, ?)",(id_livro, id_usuario, data_emprestimo, data_devolucao) )
    conn.commit()    
    conn.close()    

# Função para exibir todos os livros emprestados no momento
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                          FROM livros\
                          INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                          INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
                          WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# Exemplo das funções
#insert_book("Dom Quixote", "Miquel", "Editora 1", 1605, "123456")
#insert_user("joao", "silva", "Angola,Cabinda", "joao@gmail.com", "+244 123")
#insert_loan(1,1, "2022-09-20", None)
#livros_emprestados = get_books_on_loan()
print(get_books_on_loan())
#exibir_livros()
