from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class StoreModel(BaseModel):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(120))
    address = Column(String(255))
    telephone = Column(Integer)
    store_section_id = Column(Integer, ForeignKey('stores_locations.id'))
    status = Column(Boolean, default=True)
    
    location = relationship('StoreLocationModel', uselist=False, back_populates='stores')
    
    