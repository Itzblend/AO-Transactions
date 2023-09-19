from src.db import Database

db = Database()
# cur = db.get_cursor()

db.print_and_execute(
    "UPDATE users SET balance = balance - 100 WHERE id = 1;"
    )

proceed = input("Proceed? [Y/n] ")

if proceed.lower() == "n":
    db.rollback()
    exit()

db.print_and_execute(
    "UPDATE users SET balance = balance - 100 WHERE id = 2"
)