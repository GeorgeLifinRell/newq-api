import sqlite3

DATABASE_URL = './newq.db'

VENDORS_CREATION_QUERY = '''
    CREATE TABLE IF NOT EXISTS VENDORS (
        ID INTEGER PRIMARY KEY,
        NAME TEXT
    )
'''

SHOPS_CREATION_QUERY = '''
    CREATE TABLE IF NOT EXISTS SHOPS (
        ID INTEGER PRIMARY KEY,
        NAME TEXT,
        VENDOR_ID INTEGER REFERENCES VENDORS(ID)
    )
'''

MENU_ITEMS_CREATION_QUERY = '''
    CREATE TABLE IF NOT EXISTS MENU_ITEMS (
        id INTEGER PRIMARY KEY,
        shop_id INTEGER references SHOPS(id)
        name TEXT,
        price REAL
    )
'''

def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    return conn

def create_tables():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(VENDORS_CREATION_QUERY)
    cursor.execute(SHOPS_CREATION_QUERY)
    cursor.execute(MENU_ITEMS_CREATION_QUERY)
    conn.commit()
    conn.close()
