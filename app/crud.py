from database import get_db
from schemas import MenuItem, Shop, Vendor


# MenuItems CRUD
def get_menu_items():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MENU_ITEMS")
    menu_items = cursor.fetchall()
    conn.close()
    if menu_items is None:
        return {"message": "No items found"}
    return [{"id": row[0], "name": row[1], "price": row[2], "shop_id": row[3]} for row in menu_items]


def get_menu_item(menu_item_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MENU_ITEMS WHERE id=?", (menu_item_id,))
    menu_item = cursor.fetchone()
    conn.close()
    if menu_item is None:
        return None
    return {"id": menu_item[0], "name": menu_item[1], "price": menu_item[2], "shop_id": menu_item[3]}


def create_menu_item(menu_item: MenuItem):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO MENU_ITEMS (id, name, price, shop_id) VALUES (?, ?, ?, ?)", (menu_item.id, menu_item.name, menu_item.price, menu_item.shop_id))
    conn.commit()
    conn.close()
    return {"message": "Menu item created successfully"}


def update_menu_item(menu_item_id: int, menu_item: MenuItem):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE MENU_ITEMS SET name=?, price=? WHERE id=?", (menu_item.name, menu_item.price, menu_item_id))
    conn.commit()
    conn.close()
    return {"message": "Menu updated successfully"}


def delete_menu_item(menu_item_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM MENU_ITEMS WHERE id=?", (menu_item_id,))
    conn.commit()
    conn.close()
    return {"message": "Menu item deleted successfully"}


# Shops CRUD
def get_shops():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SHOPS")
    shops = cursor.fetchall()
    conn.close()
    return [{"id": shop[0], "name": shop[1]} for shop in shops]


def get_shop(shop_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SHOPS WHERE id=?", (shop_id))
    shop = cursor.fetchone()
    conn.close()
    if shop is None:
        return None
    return {"id": shop[0], "name": shop[1]}


def create_shop(shop: Shop):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SHOPS (id, name) VALUES (?, ?)", (shop.id, shop.name))
    conn.commit()
    conn.close()
    return {"message": "Shop created successfully"}


def update_shop(shop_id: int, shop: Shop):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE SHOPS SET id=?, name=? WHERE id=?", (shop.id, shop.name, shop_id))
    conn.commit()
    conn.close()
    return {"message": "Shop updated successfully"}


def delete_shop(shop_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SHOPS WHERE id=?", (shop_id))
    conn.commit()
    conn.close()
    return {"message": "Shop deleted successfully"}


# Vendors CRUD
def get_vendors():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VENDORS")
    vendors = cursor.fetchall()
    if vendors is None:
        return None
    conn.close()
    return [{"id": vendor[0], "name": vendor[1]} for vendor in vendors]


def get_vendor(vendor_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM VENDORS WHERE id=?', (vendor_id,))
    vendor = cursor.fetchone()
    conn.close()
    if vendor is None:
        return None
    return {"id": vendor[0], "name": vendor[1]}


def create_vendor(vendor: Vendor):
    conn = get_db()
    cursor = conn.cursor()
    if get_vendor(vendor_id=vendor.id) is not None:
        return None
    cursor.execute("INSERT INTO VENDORS (id, name) VALUES (?, ?)", (vendor.id, vendor.name))
    conn.commit()
    conn.close()
    return {"message": "Shop created successfully"}


def update_vendor(vendor_id: int, vendor: Vendor):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE VENDORS SET id=?, name=? WHERE id=?", (vendor.id, vendor.name, vendor_id))
    if cursor.rowcount() < 1:
        return None
    conn.commit()
    conn.close()
    return {"message": "Shop updated successfully"}


def delete_vendor(vendor_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM VENDORS WHERE id=?", (vendor_id))
    if cursor.rowcount() < 1:
        return None
    conn.commit()
    conn.close()
    return {"message": "Shop deleted successfully"}
