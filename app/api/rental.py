from fastapi import FastAPI, APIRouter, Request, Response


app = APIRouter(
    prefix="/rental"

)


@app.get("/detail")
def get_rental_detail(request : Request):
    conn = request.app.state.db_conn
    cur = conn.cursor()
    try:
        cur.execute("select * from rental")
        rent = cur.fetchall()
        return rent
    except Exception as err:
        raise f'Error in rental {err}'
    # rented = [{"id": 1, "model": "Toyota Camry"}, {"id": 2, "model": "Honda Accord"}]
    # return rented