import sqlite3


def create():
    conn = sqlite3.connect('pastebin_db')
    c = conn.cursor()


    c.execute('''
              CREATE TABLE IF NOT EXISTS pastebin1 ([pastebin_id] TEXT, [text_1] TEXT)
              ''')
    conn.commit()
    conn.close()
