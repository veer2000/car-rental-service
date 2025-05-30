from fastapi import FastAPI, APIRouter


app = APIRouter(prefix = "/users")


@app.get('/detail')
def get_user():
    users_detail = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return users_detail