from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from . import crud,Schema,models
from fastapi import APIRouter
from api.dependencies import get_db
from api.app.P_orders.models import P_order
from api.app.Shipments.models import shipment
#models.d.base.metadata.create_all(bind=d.engine)

router=APIRouter(prefix="/ECOMM")


@router.post("/Customer")
async def create_member(MEM: Schema.Cust, DB:Session=Depends(get_db)):
    db_customer= crud.get_member_by_phone(DB, phone=MEM.Mobile)
    if db_customer:
        raise HTTPException(status_code=400,detail="phone already exist")
    else:
        return crud.create_cust(DB=DB, MEM=MEM)


@router.get("/Order_details")
async def get_customer_order(DB:Session=Depends(get_db)):
    li=[]
    customers=DB.query(models.customer.Customer_ID).all()
    for i in customers:
        orders=DB.query(P_order).filter(P_order.Customer_ID==i.Customer_ID).all()
        li.append({"Customer_ID":i.Customer_ID,"purchaseOrder":orders})
    return li


@router.get("/Ship_order_details")
async def get_customer_order_shipment(DB:Session=Depends(get_db)):
    li=[]
    customers=DB.query(models.customer.Customer_ID).all()
    for i in customers:
        orders=DB.query(P_order.Product_name,P_order.Customer_ID,P_order.Purchase_order_ID,P_order.Quantity,P_order.MRP,P_order.Pricing,shipment).join(shipment,shipment.Purchase_order_ID==P_order.Purchase_order_ID).filter(P_order.Customer_ID==i.Customer_ID).all()
        li.append({"Customer_ID":i.Customer_ID,"purchaseOrder":orders})
    return li


