import os, psycopg2
from dotenv import load_dotenv

def DB_Connect():
    load_dotenv()
    connection_string = os.getenv("DATABASE_URL")
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    print('database conectado.')
    return cur, conn