import psycopg2

DB_URL = "host='localhost' port='5432' dbname='studenti-db' user='postgres' password='root'"

conn = psycopg2.connect(DB_URL)

def create_table():
    cur = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS studenti
    (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        cognome VARCHAR(100) NOT NULL,
        eta INTEGER NOT NULL,
        email VARCHAR(255) NOT NULL
    )
    """
    cur.execute(query)
    conn.commit()
    cur.close()

def drop_table():
    cur = conn.cursor()
    query = """
    DROP TABLE IF EXISTS studenti
    """
    cur.execute(query)
    conn.commit()
    cur.close()

def insert_students():
    cur = conn.cursor()
    query = """
    INSERT INTO studenti (nome, cognome, eta, email)
    VALUES
    ('Mario', 'Rossi', 34, 'mariorossi@gmail.com'),
    ('Giacomo', 'Bianchi', 10, 'giacomobianchi@gmail.com'),
    ('Leonardo', 'Viola', 39, 'leoviola@gmail.com'),
    ('Riccardo', 'Giallo', 40, 'riccardogiallo@gmail.com')
    """

    cur.execute(query)
    conn.commit()
    cur.close()

def get_students():
    cur = conn.cursor()
    query = """
    SELECT * FROM studenti
    """

    cur.execute(query)
    students = cur.fetchall()
    conn.commit()
    cur.close()
    return students