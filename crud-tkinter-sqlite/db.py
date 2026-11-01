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
    with connect() as conn:
        conn.execute(
            "INSERT INTO students (name, course, year, email) VALUES (?, ?, ?, ?)",
            (name, course, year, email),
        )


def get_students(search=""):
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM students "
            "WHERE name LIKE ? OR course LIKE ? ORDER BY id",
            (f"%{search}%", f"%{search}%"),
        ).fetchall()


def update_student(student_id, name, course, year, email):
    with connect() as conn:
        conn.execute(
            "UPDATE students SET name = ?, course = ?, year = ?, email = ? "
            "WHERE id = ?",
            (name, course, year, email, student_id),
        )


def delete_student(student_id):
    with connect() as conn:
        conn.execute("DELETE FROM students WHERE id = ?", (student_id,))


if __name__ == "__main__":
    add_student("Maria Santos", "BSIT", 3, "maria@example.com")
    add_student("John Reyes", "BSCS", 2, "john@example.com")
    for row in get_students():
        print(row)
