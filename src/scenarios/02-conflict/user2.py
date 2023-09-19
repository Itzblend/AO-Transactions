from src.db import Database

db = Database()

db.print_and_execute(
    "UPDATE users SET balance = balance + 100 WHERE id = 2;"
)

input("So far so good...")

db.print_and_execute(
    "UPDATE users SET balance = balance - 100 WHERE id = 1;"
)

print("Finished Transaction!")

db.commit()