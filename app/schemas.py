from pydantic import BaseModel

# Vendor Model
class Vendor(BaseModel):
    id: int
    name: str

class VendorCreate(Vendor):
    pass

class VendorUpdate(Vendor):
    pass

class VendorDelete(Vendor):
    pass

# Shop Model
class Shop(BaseModel):
    id: int
    name: str
    vendor_id: int

class ShopCreate(Shop):
    pass

class ShopUpdate(Shop):
    pass

class ShopDelete(Shop):
    pass

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

class MenuItemDelete(MenuItem):
    pass