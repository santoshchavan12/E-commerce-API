from sqlalchemy.orm import Session
from . import models,schema

def create_shipment(DB:Session, SHIP: schema._create_shipment):
    db_shipment= models.shipment(Address=SHIP.City,City=SHIP.City, Pincode=SHIP.Pincode,Purchase_order_ID=SHIP.Purchase_order_ID,Customer_ID=SHIP.Customer_ID)
    DB.add(db_shipment)
    DB.commit()
    DB.refresh(db_shipment)
    return db_shipment
#
# def get_booking_detalis(app:Session,bookid:int):
#     return app.query(models.shipment).filter(bookid == models.bookings.bookid).first()

