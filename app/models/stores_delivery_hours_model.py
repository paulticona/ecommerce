from app.models.base import BaseModel
from sqlalchemy import Column, Time, Integer, Boolean, ForeignKey, Date, String
from sqlalchemy.orm import relationship


class HolidayModel(BaseModel):
    __tablename__ = 'holidays'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)  # Lunes -> 0 && Domingo -> 6
    description = Column(String(160))
    status = Column(Boolean, default=True)
