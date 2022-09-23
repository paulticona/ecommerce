from app.models.base import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
class StoreLocationModel(BaseModel):
    __tablename__ = 'stores_locations'

    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(120))
    status = Column(Boolean, default=True)

    stores = relationship('StoreModel', uselist=True, back_populates='location')