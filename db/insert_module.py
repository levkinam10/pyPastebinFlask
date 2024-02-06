import sqlite3
import random
import string


def id_dedicate():
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(9))
    # result_str = '923567890'
    tuple_simple = (1,2)
    conn = sqlite3.connect('db_data/pastebin_db')
    c = conn.cursor()
    c.execute("SELECT 1 FROM pastebin1 WHERE pastebin_id = ?", (result_str,))
    res = (type(c.fetchone()) == type(tuple_simple))
    #print(res)
    #if res: return tuple_simple
    #else: return 0
    if res:
        conn.close()
        return id_dedicate()

    else:
        conn.close()
        return result_str


def db_insert(text):
    id1 = id_dedicate()
    conn = sqlite3.connect('db_data/pastebin_db')
    c = conn.cursor()
    c.execute('INSERT INTO pastebin1 (pastebin_id, text_1) VALUES (?, ?)', (id1, text))
    conn.commit()
    conn.close()
    return id1

