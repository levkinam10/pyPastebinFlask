import sqlite3


def db_search(id1):
    tuple_simple = (1,2)
    conn = sqlite3.connect('pastebin_db')
    c = conn.cursor()
    c.execute('SELECT * FROM pastebin1 WHERE pastebin_id = ?', (id1,))
    res = c.fetchone()
    c.close()
    if type(res) == type(tuple_simple):
        return res[1]
    else: return None
