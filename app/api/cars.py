from fastapi import FastAPI, APIRouter, Response
from fastapi.responses import JSONResponse

app = APIRouter(
    prefix = '/cars'
)


@app.get("/detail")
def get_cars_detail():
    cars = [{"car1" : "volvo", "car2": "honda", "car3": "Tata"}] 
    return  cars
