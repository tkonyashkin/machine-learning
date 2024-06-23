from fastapi import FastAPI, Depends, HTTPException
import datetime
from pydantic import BaseModel
import json
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db() -> psycopg2.connect:
    conn = psycopg2.connect("postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml", cursor_factory=RealDictCursor)
    return conn
    


app = FastAPI()

# @app.get("/")
# def say_hello():
#     return "hello, world"

# {
#   "name": <строка>,
#   "surname": <строка>,
#   "age": <число>,
#   "registration_date": <дата в формате YYYY-MM-DD>
# }

class UserAdd(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date
    
    class Сonfig:
        orm_mode = True

class PostResponse(BaseModel):
    id: int
    text: str
    topic: str
    
    class Config:
        orm_mode = True
    

@app.get("/")
def sum_two(a: int, b:int) -> int:
    return a + b

@app.get("/sum_date")
def sum_date(current_date: datetime.date, offset: int) -> datetime.date:
    return current_date + datetime.timedelta(days=offset)

@app.post("/user/validate")
def make_user(user: UserAdd) -> str:
    return f"Will add user: {user.name} {user.surname} with age {user.age}"

@app.get("/user/{id}")
def get_user(id: int, db = Depends(get_db)):
    with db.cursor() as cursor:
        query = f"""
                SELECT gender, age, city FROM "user"
                WHERE id = %(id)s
                """
        cursor.execute(query, {'id': id})
        json_data = cursor.fetchone()
        if not json_data:
            raise HTTPException(status_code=404, detail="user not found")
        else:
            return json_data
        
        
@app.get("/post/{id}", response_model=PostResponse)
def get_post(id: int, db = Depends(get_db)) -> PostResponse:
    with db.cursor() as cursor:
        query = """
                SELECT id, text, topic
                FROM post
                WHERE id = %(id)s
                """
        cursor.execute(query, {'id': id})
        json_data = cursor.fetchone()
        if not json_data:
            raise HTTPException(status_code=404, detail="post not found")
        else:
            return PostResponse(**json_data)