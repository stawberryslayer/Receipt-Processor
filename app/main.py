from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
from app.processor import calculate_points

app = FastAPI()
receipts = {}

class Item(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[Item]
    total: str

@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    receipts[receipt_id] = points
    return {"id": receipt_id}

@app.get("/receipts/{receipt_id}/points")
def get_points(receipt_id: str):
    if receipt_id in receipts:
        return {"points": receipts[receipt_id]}
    raise HTTPException(status_code=404, detail="Receipt not found")
