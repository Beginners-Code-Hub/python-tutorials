import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE students (name TEXT)")
conn.execute("INSERT INTO students VALUES ('Maria')")
conn.execute("INSERT INTO students VALUES ('John')")

search = "x' OR '1'='1"  # typed into the search box

# BAD: the text becomes part of the SQL
sql = f"SELECT * FROM students WHERE name = '{search}'"
print(conn.execute(sql).fetchall())

# GOOD: ? keeps it as plain data
sql = "SELECT * FROM students WHERE name = ?"
print(conn.execute(sql, (search,)).fetchall())
