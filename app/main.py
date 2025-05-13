from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
from app.processor import calculate_points
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_400_BAD_REQUEST

app = FastAPI()
receipts = {}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"detail": "The receipt is invalid."},
    )

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

@app.get("/receipts/{id}/points")
def get_points(id: str):
    if id in receipts:
        return {"points": receipts[id]}
    raise HTTPException(status_code=404, detail="No receipt found for that ID.")
