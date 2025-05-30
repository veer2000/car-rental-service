from fastapi import FastAPI
from api import cars, rental, users
from db import database
from contextlib import asynccontextmanager





@asynccontextmanager
async def lifespan(app : FastAPI):
    #statup establish connection
    app.state.db_conn = database.db_connection()
    yield
    app.state.db_conn.close()


app = FastAPI(lifespan=lifespan)

app.include_router(cars.app)
app.include_router(rental.app)
app.include_router(users.app)


@app.get("/home")
def default_route():
    return {'message': 'Hello, World!'}
