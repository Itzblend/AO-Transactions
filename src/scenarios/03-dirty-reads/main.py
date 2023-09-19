import psycopg2
from multiprocessing import Pool
from src.db import Database
from time import sleep



# Function to read user records from the database
def read_user(user_id):
    db = Database()
    cursor = db.get_cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    record = cursor.fetchone()
    cursor.close()
    
    print(f"Read user {user_id}: {record}")
    db.close_connection

# Create a pool of workers to simulate concurrent read operations
with Pool(3) as pool:
    # Read user record concurrently
    pool.map(read_user, [1, 1, 1])

