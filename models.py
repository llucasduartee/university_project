import datetime as _dt
import sqlalchemy as _sql
import database as _database

class Student(_database.Base):
    __tablename__ = "students"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, index=True)
    password = _sql.Column(_sql.String, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    classes = _sql.Column(_sql.JSON)
    isActive = _sql.Column(_sql.Boolean, default=True)
    semester = _sql.Column(_sql.Integer, index=True)
    course = _sql.Column(_sql.String)