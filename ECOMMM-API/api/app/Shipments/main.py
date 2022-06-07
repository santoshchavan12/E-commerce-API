
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from . import crud,schema,models
from fastapi import APIRouter
from api.dependencies import get_db
#models.d.base.metadata.create_all(bind=d.engine)

router=APIRouter()


@router.post("/ECOMM/SHIP")
def create_shipment(request: schema._create_shipment, DB:Session=Depends(get_db)):
    #if BOOK.memid in models.member.memberid and BOOK.movieid in models.movies.movie_id:

       return crud.create_shipment(SHIP=request, DB=DB)
    #else:
        #raise HTTPException(status_code=410,detail="FOREIGN KEY")


@router.get("/ECOMM/GET_SHIPMENTS")
def get_detalis(CITY_NAME:str,DB:Session=Depends(get_db)):
    db_shipments= DB.query(models.shipment).filter(models.shipment.City==CITY_NAME).all()
    if db_shipments is None:
        raise HTTPException(status_code=404,detail="invalid input")
    else:
        return db_shipments