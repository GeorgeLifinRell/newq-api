from database import get_db
from schemas import MenuItem, Shop


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