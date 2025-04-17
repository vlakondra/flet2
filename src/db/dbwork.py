import sqlite3

class dbWork():
    def __init__(self, db_name):
        self.dbpath = f'storage/data/{db_name}'
        conn = sqlite3.connect(self.dbpath) #f'storage/data/{db_name}') 
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                fam TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def add_user(self, name, last_name, fam):
        conn = sqlite3.connect(self.dbpath)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, last_name,fam) VALUES (?, ?, ?)", (name, last_name, fam))
        conn.commit()
        conn.close()

    def get_users(self):
        conn = sqlite3.connect(self.dbpath)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users    