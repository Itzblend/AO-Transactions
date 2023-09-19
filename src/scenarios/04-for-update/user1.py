from src.db import Database

db = Database()

db.print_and_execute(
    """
    SELECT * FROM reservations
    WHERE room_id = 'room1' AND start_time = '12:00:00'
    AND end_time = '13:00:00' AND reserved = false FOR UPDATE;
"""
)

proceed = input("Proceed? [Y/n] ")

if proceed.lower() == "n":
    db.rollback()
    exit()

db.print_and_execute(
    """
    UPDATE reservations
    SET reserved = true,
        reserved_by = 'user1'
    WHERE room_id = 'room1' AND start_time = '12:00:00'
    AND end_time = '13:00:00';
    """
)

db.commit()
print("Finished Transaction!")