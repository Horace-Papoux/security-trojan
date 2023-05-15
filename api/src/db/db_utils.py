import sqlite3
import os.path

def get_db_connection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database.db")
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def clean_db():
    conn = get_db_connection()
    conn.execute('DELETE FROM accounts')
    conn.commit()
    conn.close()

