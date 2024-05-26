from pydantic import BaseModel

# Shop Model
class Shop(BaseModel):
    id: int
    name: str

class ShopCreate(Shop):
    pass

class ShopUpdate(Shop):
    pass

class ShopResponse(Shop):
    id: int

# Menu Items Model
class MenuItem(BaseModel):
    id: int
    shop_id: int
    name: str
    price: float

class MenuItemCreate(MenuItem):
    pass

class MenuItemUpdate(MenuItem):
    pass

class MenuItemResponse(MenuItem):
    id: int
