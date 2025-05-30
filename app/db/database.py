import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("POSTGRES_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_PORT = os.getenv("POSTGRES_POST")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_SCHEMA = os.getenv("POSTGRES_SCHEMA")

print(DB_PASSWORD)
 

def db_connection():
    try:
        conn = psycopg2.connect( 
                                host = DB_HOST, 
                                database = DB_NAME, 
                                user = DB_USER, 
                                password = DB_PASSWORD, 
                                options=f"-c search_path={DB_SCHEMA}",
                                cursor_factory= RealDictCursor
        )
        return conn
    except Exception as err:
        raise f'Exception in Database connection {err}' 
