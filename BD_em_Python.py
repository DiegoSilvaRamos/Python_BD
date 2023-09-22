import sqlite3 as conector

conexão = None
cursor = None


# Abertura de conexão
try:
    conexão = conector.connect("Meu_Banco_Dados.db")
    cursor = conexão.cursor()

    # Execução de um comando
    comando = '''CREATE TABLE PESSOA(
    cpf INTEGER NOT NULL,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL,
    oculos BOOLEAN NOT NULL,
    PRIMARY KEY(cpf)
    );'''

    cursor.execute(comando)

    # Efetivação do comando
    conexão.commit()

except conector.DatabeseError as error:
    print("Erro de Banco de Dados", error)

finally:
    # fechamento das conexões e Cursores
    if cursor:
        cursor.closed()
    if conexão:
        conexão.closed()
