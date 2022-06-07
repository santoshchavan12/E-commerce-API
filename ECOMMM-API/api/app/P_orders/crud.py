from sqlalchemy.orm import Session
from . import models,schema



def create_order(DB:Session, MOV: schema.P_order):
    db_order= models.P_order(Customer_ID=MOV.Customer_ID,  Product_name=MOV.Product_name,Quantity=MOV.Quantity,MRP=MOV.MRP,Pricing=MOV.Pricing)
    DB.add(db_order)
    DB.commit()
    DB.refresh(db_order)
    return db_order

def get_product_by_product_name(DB:Session,name:str):
    return DB.query(models.P_order).filter(name == models.P_order.Product_name).first()
