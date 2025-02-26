from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from db import (
    create_table,
    drop_table,
    insert_students,
    get_students
)
from pydantic import BaseModel

app = FastAPI(debug=True)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    email: str

students = [Student(id=s[0], first_name=s[1], last_name=s[2], age=s[3], email=s[4]) for s in get_students()]

@app.get("/")
def index():
    return {"studenti": students}

if __name__ == '__main__':
    drop_table()
    create_table()
    insert_students()
    uvicorn.run(app, host="127.0.0.1", port=8000)
