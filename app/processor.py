import math
from fastapi import HTTPException
def calculate_points(receipt):
    pts = 0
    #points for retailer name(character, not ws or special char)
    
    pts += sum(c.isalnum() for c in receipt.retailer)
    

    #round dollar amount
    cents = receipt.total.split('.')[-1]
    if cents =='00':
        pts+=50
    
    #multiple of 0.25
    if cents in ['25','50','75','00']:
        pts+=25

    #every two items
    num_items = len(receipt.items)
    pts += (num_items//2)*5

    #item description is a multiple of 3
    items = receipt.items
    for item in items:
        if len(item.shortDescription.strip()) % 3==0:
            pts += math.ceil(float(item.price) * 0.2)
        
    #date
    try:
        purchase_date = receipt.purchaseDate.split('-')
        if len(purchase_date)!= 3:
            raise ValueError("Invalid date format")
        if int(purchase_date[-1]) % 2 == 1:
            pts+=6
    except (IndexError, ValueError):
       raise HTTPException(status_code=400, detail="The receipt is invalid.")


    #purchase time
    try:
        purchase_time = receipt.purchaseTime.split(':')
        if len(purchase_time)!= 2:
            raise ValueError("Invalid time format")
        if purchase_time[0] == "14" or purchase_time[0]== "15":
            pts+=10
    except (IndexError, ValueError):
        raise HTTPException(status_code=400, detail="The receipt is invalid.")



    return pts