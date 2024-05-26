from fastapi import APIRouter, HTTPException
from typing import List
from schemas import *
from crud import *

router = APIRouter()

# Routes for MenuItems
@router.get("/foods/", response_model=List[MenuItemResponse])
async def read_items():
    return get_menu_items()

@router.get("/menu_item/{item_id}", response_model=MenuItemResponse)
async def read_item(item_id: int):
    item = get_menu_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

@router.post("/menu_item/")
async def create_item_endpoint(item: MenuItemCreate):
    return create_menu_item(item)

@router.put("/menu_item/{item_id}")
async def update_item_endpoint(item_id: int, item: MenuItemUpdate):
    return update_menu_item(item_id, item)

@router.delete("/menu_item/{item_id}")
async def delete_item_endpoint(item_id: int):
    return delete_menu_item(item_id)

# Routes for Shops
@router.get("/shops/", response_model=List[ShopResponse])
async def read_shops():
    return get_shops()

@router.get("/shops/{shop_id}", response_model=ShopResponse)
async def read_shop(shop_id: int):
    shop = get_shop(shop_id)
    if shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return shop

@router.post("/shops/")
async def create_shop_endpoint(shop: ShopCreate):
    return create_shop(shop)

@router.put("/shops/{shop_id}")
async def update_shop_endpoint(shop_id: int, shop: ShopUpdate):
    return update_shop(shop_id, shop)

@router.delete("/shops/{shop_id}")
async def delete_shop_endpoint(shop_id: int):
    return delete_shop(shop_id)
