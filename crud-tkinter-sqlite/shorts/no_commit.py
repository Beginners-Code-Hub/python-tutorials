import sqlite3

SQL = "INSERT INTO students VALUES (?)"


def connect():
    conn = sqlite3.connect("short.db")
    conn.execute("CREATE TABLE IF NOT EXISTS "
                 "students (name TEXT)")
    return conn


def add_student(name):
    conn = connect()
    conn.execute(SQL, (name,))


add_student("Maria")
print(connect().execute(
    "SELECT * FROM students").fetchall())
