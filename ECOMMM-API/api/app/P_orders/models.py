from sqlalchemy import Column,Integer, String,ForeignKey
from api.database import base




class P_order(base):
    __tablename__="P_orders"
    Purchase_order_ID=Column(Integer,primary_key=True,index=True)
    Customer_ID=Column(Integer,ForeignKey("customer.Customer_ID"),nullable=False)
    Product_name=Column(String)
    Quantity=Column(Integer)
    MRP=Column(Integer)
    Pricing=Column(Integer)
