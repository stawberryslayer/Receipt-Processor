import math
def calculate_points(receipt):
    pts = 0
    #points for retailer name(character, not ws or special char)
    pts += sum(c.isalnum() for c in receipt["retailer"])
    

    #round dollar amount
    cents = receipt["total"].split('.')[-1]
    if cents =='00':
        pt+=50
    
    #multiple of 0.25
    if cents in ['25','50','75']:
        pt+=25

    #every two items
    num_items = len(receipt["items"])
    pts += (num_items//2)*5

    #item description is a multiple of 3
    items = receipt["items"]
    for item in items:
        if item['shortDescription'].strip() % 3==0:
            pts += math.ceil(item['price'] * 0.2)
        
    #date
    purchase_date = receipt["purchaseDate"].split('-')[-1]
    if purchase_date % 2 ==1:
        pts+=6

    #purchase time
    purchase_hr = receipt["purchaseTime"].split(':')[0]
    if purchase_hr == 13 or purchase_hr == 14:
        pts+=10


    return pts