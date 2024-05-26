import sqlite3

DATABASE_URL = './newq.db'

def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    return conn

def create_tables():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MENU_ITEMS (
            id INTEGER PRIMARY KEY,
            shop_id INTEGER references SHOPS(id)
            name TEXT,
            price REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SHOPS (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')
    conn.commit()
    conn.close()
