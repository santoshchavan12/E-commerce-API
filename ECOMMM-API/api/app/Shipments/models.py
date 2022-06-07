from sqlalchemy import Column,Integer, ForeignKey,String
from api.database import base

class shipment(base):
    __tablename__="shipment"
    Address=Column(String,nullable=False)
    City=Column(String,nullable=False)
    Pincode=Column(Integer,nullable=False)
    Purchase_order_ID=Column(Integer,ForeignKey("P_orders.Purchase_order_ID"),primary_key=True)
    Customer_ID=Column(Integer,ForeignKey("customer.Customer_ID"),primary_key=True,nullable=False)