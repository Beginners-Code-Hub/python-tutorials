import sqlite3

DB_FILE = "students.db"


def connect():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            course TEXT NOT NULL,
            year   INTEGER NOT NULL,
            email  TEXT
        )
    """)
    return conn


