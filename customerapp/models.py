from django.db import models

# Create your models here.
class item:
    item_id:str
    item_image:str
    item_name:str
    item_desc:str
    item_cost:int
    quantity:int
class msgs:
    id:int
    username:str
    email:str
    message:str
class order:
    order_id:int
    username:str
    #cust_id:int
    ordered_date:int
    deliverystatus:str
    totalamount:int
class Profile:
    id:int
    name:str
    email:str
    phoneNumber:int
    address:str
    