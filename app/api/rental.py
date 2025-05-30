from fastapi import FastAPI, APIRouter, Response


app = APIRouter(
    prefix="/rental"

)


@app.get("/detail")
def get_rental_detail():
    rented = [{"id": 1, "car_id": 1, "user_id": 2, "status": "active"}]
    return rented