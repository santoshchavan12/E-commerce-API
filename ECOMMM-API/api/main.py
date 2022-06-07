from fastapi import FastAPI
import uvicorn
from api.database import engine
from api.app.Customer import main as cust_main, models as cust_model
from api.app.P_orders import models as order_model, main as order_main
from api.app.Shipments import main as shipment_main
from api.app.Shipments import models as shipment_model

cust_model.base.metadata.create_all(bind=engine)
order_model.base.metadata.create_all(bind=engine)
shipment_model.base.metadata.create_all(bind=engine)


app=FastAPI(title="ECOMM")

app.include_router(cust_main.router)
app.include_router(order_main.router)
app.include_router(shipment_main.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)