# ids after student 1 was deleted
rows = [(2, "John Reyes"), (3, "Ana Cruz")]
clicked = 0  # you clicked the first row (John)

# BAD: row position + 1 is not the database id
print("BAD  deletes id", clicked + 1)

# GOOD: iid=row[0] gives the real id back
print("GOOD deletes id", rows[clicked][0])
