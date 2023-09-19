import psycopg2

class Database:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )

    def get_connection(self):
        return self.conn
    
    def close_connection(self):
        self.conn.close()

    def get_cursor(self):
        return self.conn.cursor()
    
    def close_cursor(self, cursor):
        cursor.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def print_and_execute(self, query):
        print(query)
        cur = self.get_cursor()
        cur.execute(query)
        return cur

    def reset_balance(self):
        cur = self.get_cursor()
        cur.execute("UPDATE users SET balance = id * 100;")
        self.commit()

    def reset_reservations(self):
        cur = self.get_cursor()
        cur.execute("UPDATE reservations SET reserved = false;")
        self.commit()





if __name__ == "__main__":
    db = Database()
    cur = db.get_cursor()
    cur.execute("SELECT 42;")
    print(cur.fetchone()[0])