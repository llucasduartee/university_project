from typing import TYPE_CHECKING 
import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_student(student: _schemas.CreateStudent, db: "Session") -> _schemas.Student:
    student = _models.Student(**student.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return _schemas.Student.from_orm(student)