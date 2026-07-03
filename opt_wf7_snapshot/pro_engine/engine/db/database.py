from pathlib import Path
import sqlite3
import json
from datetime import datetime


DB=Path("data/wf.db")


def connect():
    DB.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB)


def init():

    c=connect()

    c.execute("""
    CREATE TABLE IF NOT EXISTS events(
    id INTEGER PRIMARY KEY,
    time TEXT,
    source TEXT,
    kind TEXT,
    severity TEXT,
    details TEXT
    )
    """)

    c.commit()
    c.close()



def insert(event):

    c=connect()

    c.execute(
    """
    INSERT INTO events
    VALUES(NULL,?,?,?,?,?)
    """,
    (
    datetime.now().isoformat(),
    event.get("source"),
    event.get("kind"),
    event.get("severity"),
    json.dumps(event.get("details"))
    ))

    c.commit()
    c.close()



def count():

    c=connect()

    r=c.execute(
    "select count(*) from events"
    ).fetchone()

    c.close()

    return r[0]

