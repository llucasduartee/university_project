import datetime as _dt
import pydantic as _pydantic

class _BaseStudent(_pydantic.BaseModel):
    name: str
    email: str
    password: str
    classes: list[dict[str, dict[str, int]]]
    semester: int
    course: str

class Student(_BaseStudent):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True

class CreateStudent(_BaseStudent):
    pass