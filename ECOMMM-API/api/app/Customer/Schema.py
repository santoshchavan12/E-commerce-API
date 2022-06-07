
from pydantic import BaseModel

class Cust(BaseModel):
    Mobile:int
    Customer_name:str
    Email:str
    City:str


class New_Cust(Cust):
    Customer_id:int
    class Config:
         orm_mode=True

