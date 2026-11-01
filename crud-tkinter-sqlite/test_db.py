import db

db.add_student("Maria Santos", "BSIT", 3, "maria@example.com")
db.add_student("John Reyes", "BSCS", 2, "john@example.com")

db.update_student(2, "John Reyes", "BSCS", 3, "john@example.com")
print("after update:", db.get_students("john"))

db.delete_student(2)
print("after delete:", db.get_students())
