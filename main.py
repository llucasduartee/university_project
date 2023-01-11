import fastapi as FastAPI
from pydantic import BaseModel
import schemas as _schemas
import services as _services
from typing import TYPE_CHECKING
import sqlalchemy.orm as _orm
import bcrypt


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = FastAPI.FastAPI()




@app.get('/')
async def root():
    return {"message": "Welcome to the Fake University API"}


@app.post('/register', response_model=_schemas.Student)
async def register_student(student: _schemas.CreateStudent, db: _orm.Session = FastAPI.Depends(_services.get_db)):
    bytes_password = student.password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes_password, salt)
    student.password = hash
    return await _services.create_student(student=student, db=db)
