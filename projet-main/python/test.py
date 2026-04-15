import sqlite3
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def init_bd():
    conn = sqlite3.connect(os.path.join(BASE_DIR, 'cle.db'))
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cle TEXT NOT NULL,
        taille INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

init_bd()

def ajouter_cle(cle):
    conn = sqlite3.connect(os.path.join(BASE_DIR, 'cle.db'))
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cles (cle, taille)
        VALUES (?, ?)
    ''', (cle, len(cle)))
    conn.commit()
    conn.close()