from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from . import crud,schema,models
from fastapi import APIRouter
from api.dependencies import get_db
#models.d.base.metadata.create_all(bind=d.engine)

router=APIRouter()

@router.post("/ECOMM/Order")
def create_order(request: schema.P_order, DB:Session=Depends(get_db)):
        if request.Pricing>request.MRP:
                return HTTPException(status_code=400,detail="PRicing cant be more than MRP")
        return crud.create_order(DB=DB, MOV=request)

# @router.get("/BUDDINGBOOKING/GET_MOVIE", response_model=schema._createmovie)
# def get_movie(movie_name:str,app:Session=Depends(get_db)):
#     db_movie= crud.get_movie_ny_moviename(app=app, name=movie_name)
#     if db_movie is None:
#         raise HTTPException(status_code=404,detail="invalid input")
#     return db_movie
