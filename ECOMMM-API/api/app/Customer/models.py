from sqlalchemy import Column,Integer, String, DateTime, Text,NUMERIC
from datetime import datetime
from api.database import base

class customer(base):
   __tablename__="customer"
   Customer_ID=Column(Integer,primary_key=True,index=True)
   Customer_name=Column(String,nullable=False)
   Email=Column(String,unique=True)
   Mobile=Column(NUMERIC,unique=True)
   City=Column(String,nullable=False)

