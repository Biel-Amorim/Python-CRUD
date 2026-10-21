import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pwd = os.getenv("DB_PASSWORD")

def conec():
    try:
        conn = psycopg.connect(
            dbname=db_name,
            user= db_user,
            password=db_pwd)

        print('Conectaod no postgres com sucesso, patrão :)')

        return conn

    except psycopg.Error as e:
        print('shiii deu erro cara')
        print(e)
        return

def close_conec(conn):
    if conn: # that mean True
        conn.close
        print('Patrão relaxe, não vai ter vazamento de dados já que encerrou')
    else:
        print('it always close')
    return

