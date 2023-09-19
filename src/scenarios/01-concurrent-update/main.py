import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from threading import Thread
from src.db import Database
import sys

def update_user_balance(user_id, new_salary):
    # Connect to the database
    db = Database()
    cur = db.get_cursor()
    
    try:
        # Begin a transaction
        db.conn.autocommit = False
        
        # Execute the update query
        cur.execute(sql.SQL("UPDATE users SET balance = %s WHERE id = %s")
                    .format(sql.Identifier('balance'), sql.Identifier('id')),
                    (new_salary, user_id))
        
        # Commit the transaction
        db.conn.commit()
        print(f"User {user_id} salary updated to {new_salary}")
        
    except psycopg2.extensions.TransactionRollbackError:
        print(f"Transaction conflict occurred for Employee {user_id}")
        db.rollback()
        
    finally:
        # Close the cursor and connection
        db.close_cursor(cur)
        db.close_connection()

# Function to simulate concurrent updates
def simulate_concurrent_updates():
    # Update employee salary on two different threads
    thread1 = Thread(target=update_user_balance, args=(1, 50000))
    thread2 = Thread(target=update_user_balance, args=(1, 60000))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()


args = sys.argv[1:]
# Call the function to simulate concurrent updates
simulate_concurrent_updates()
if args and args[0] == "-y":
    # Print the final balance
    db = Database()
    cur = db.get_cursor()
    cur.execute("SELECT id, balance FROM users WHERE id = 1;")
    print("Final balance:")
    row = cur.fetchone()
    print(f"User {row[0]}: {row[1]}")
    db.close_cursor(cur)
    db.close_connection()