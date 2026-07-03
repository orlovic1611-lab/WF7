
import sqlite3


DB="/opt/wf/database/wf.db"


def init():

    con=sqlite3.connect(DB)

    cur=con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS scans(
    id INTEGER PRIMARY KEY,
    target TEXT,
    result TEXT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    con.commit()
    con.close()



def add(target,result):

    con=sqlite3.connect(DB)

    cur=con.cursor()

    cur.execute(
    "INSERT INTO scans(target,result) VALUES(?,?)",
    (target,result)
    )

    con.commit()
    con.close()



def history():

    con=sqlite3.connect(DB)

    cur=con.cursor()

    return cur.execute(
    "SELECT * FROM scans ORDER BY id DESC"
    ).fetchall()

