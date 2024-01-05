import sqlite3


def db_delete(id1):
    conn = sqlite3.connect('pastebin_db')
    c = conn.cursor()
    c.execute('DELETE FROM pastebin1 WHERE pastebin_id = ?', (id1,))
    conn.commit()
    conn.close()
    return 200
