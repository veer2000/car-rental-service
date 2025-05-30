from fastapi import FastAPI
from api import cars, rental, users

app = FastAPI()


app.include_router(cars.app)
app.include_router(rental.app)
app.include_router(users.app)


@app.get("/")
def default_route():
    return {'message': 'Hello, World!'}
