from fastapi import APIRouter, HTTPException
from typing import List
from schemas import *
from crud import *

router = APIRouter()

# Routes for MenuItems
@router.get("/foods/", response_model=List[MenuItem])
async def read_items():
    return get_menu_items()

@router.get("/menu_item/{item_id}", response_model=MenuItem)
async def read_item(item_id: int):
    item = get_menu_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

@router.post("/menu_item/", response_model=MenuItemCreate)
async def create_item_endpoint(item: MenuItem):
    return create_menu_item(item)

@router.put("/menu_item/{item_id}", response_model=MenuItemUpdate)
async def update_item_endpoint(item_id: int, item: MenuItem):
    return update_menu_item(item_id, item)

@router.delete("/menu_item/{item_id}", response_model=MenuItemDelete)
async def delete_item_endpoint(item_id: int):
    return delete_menu_item(item_id)

# Routes for Shops
@router.get("/shops/", response_model=List[Shop])
async def read_shops():
    if get_shops() is None:
        raise HTTPException(status_code=404, detail="No Vendors to be displayed")
    return get_shops()

@router.get("/shops/{shop_id}", response_model=Shop)
async def read_shop(shop_id: int):
    shop = get_shop(shop_id)
    if shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return shop

@router.post("/shops/", response_model=ShopCreate)
async def create_shop_endpoint(shop: Shop):
    if shop is None:
        return create_shop(shop)
    else:
        raise HTTPException(status_code=400, detail="Shop already exists")

@router.put("/shops/{shop_id}", response_model=ShopUpdate)
async def update_shop_endpoint(shop_id: int, shop: Shop):
    shop = get_shop(shop_id=shop_id)
    if shop is None:
        raise HTTPException(status_code=404, detail="No such shop")
    return update_shop(shop_id, shop)

@router.delete("/shops/{shop_id}", response_model=ShopDelete)
async def delete_shop_endpoint(shop_id: int):
    shop = get_shop(shop_id=shop_id)
    if shop is None:
        raise HTTPException(status_code=404, detail="No such shop")
    return delete_shop(shop_id)


# Routes for Vendors
@router.get("/vendors/", response_model=List[Vendor])
async def read_vendors():
    if get_vendors() is None:
        raise HTTPException(status_code=404, detail="No Vendors to be displayed")
    return get_vendors()

@router.get("/vendors/{vendor_id}", response_model=Vendor)
async def read_vendor(vendor_id: int):
    vendor = get_vendor(vendor_id)
    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor

@router.post("/vendors/")
async def create_vendor_endpoint(vendor: Vendor):
    vendor = get_vendor(vendor_id=vendor.id)
    if vendor is None:
        return create_vendor(vendor)
    else:
        raise HTTPException(status_code=400, detail="Vendor already exists")

@router.put("/vendors/{vendor_id}")
async def update_vendor_endpoint(vendor_id: int, vendor: Vendor):
    vendor = get_vendor(vendor_id=vendor_id)
    if vendor is None:
        raise HTTPException(status_code=404, detail="No such vendor")
    return update_vendor(vendor_id, vendor)

@router.delete("/vendors/{vendor_id}")
async def delete_vendor_endpoint(vendor_id: int):
    vendor = get_vendor(vendor_id=vendor_id)
    if vendor is None:
        raise HTTPException(status_code=404, detail="No such vendor")
    return delete_vendor(vendor_id)
