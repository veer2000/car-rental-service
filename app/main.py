from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def default_route():
    return {'message': 'Hello, World!'}