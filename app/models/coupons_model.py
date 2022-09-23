from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, String, Float, DateTime
from sqlalchemy.orm import relationship


class CouponModel(BaseModel):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50))
    procentage = Column(Float(precision=2))  # Lunes -> 0 && Domingo -> 6
    started_ad = Column(DateTime)
    ended_ad = Column(DateTime)
    status = Column(Boolean, default=True)
 