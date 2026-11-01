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


def add_student(name, course, year, email):
    conn = connect()
    conn.execute(
        "INSERT INTO students (name, course, year, email) VALUES (?, ?, ?, ?)",
        (name, course, year, email),
    )


add_student("Maria Santos", "BSIT", 3, "maria@example.com")
print(connect().execute("SELECT * FROM students").fetchall())
