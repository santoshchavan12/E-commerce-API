from typing import List,Optional
import datetime
from pydantic import BaseModel,Field

class _create_shipment(BaseModel):
    Address :str
    City :str
    Pincode :int
    Purchase_order_ID :int
    Customer_ID:int

    class Config:
         orm_mode=True