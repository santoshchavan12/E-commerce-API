from sqlalchemy.orm import Session
from . import models,Schema


def get_member_by_phone(DB:Session,phone:str):
    return DB.query(models.customer).filter(phone == models.customer.Mobile).first()



def create_cust(DB:Session, MEM: Schema.Cust):
    db_cust= models.customer(Customer_name=MEM.Customer_name,Mobile=MEM.Mobile,City=MEM.City,Email=MEM.Email)

    DB.add(db_cust)
    DB.commit()
    DB.refresh(db_cust)
    return db_cust