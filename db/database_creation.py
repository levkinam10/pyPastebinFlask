import sqlite3
import os

def create():
    if not os.path.exists("db_data"):
        os.makedirs("db_data")
    conn = sqlite3.connect('db_data/pastebin_db')
    c = conn.cursor()


    c.execute('''
              CREATE TABLE IF NOT EXISTS pastebin1 ([pastebin_id] TEXT, [text_1] TEXT)
              ''')
    conn.commit()
    conn.close()
