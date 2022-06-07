from typing import List,Optional
import datetime
from pydantic import BaseModel,Field


class P_order(BaseModel):

    Customer_ID :int
    Product_name :str
    Quantity :int
    MRP :int
    Pricing:int

class create_Order(P_order):
    Purchase_order_ID: int
    class Config:
         orm_mode=True