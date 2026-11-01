import sqlite3

conn = sqlite3.connect("errors.db")
conn.execute("CREATE TABLE IF NOT EXISTS t (name TEXT)")
conn.execute("INSERT INTO t VALUES (?)", ("Maria",))
conn.close()  # no commit: the insert is lost

conn = sqlite3.connect("errors.db")
print(conn.execute("SELECT * FROM t").fetchall())
