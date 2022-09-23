from app.models.base import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Boolean, Text, Float, ForeignKey
class ProductModel(BaseModel):

    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(255))
    description = Column(Text)
    price = Column(Float(precision=2)) #hasta dos decimales
    image = Column(String(255))
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    status = Column(Boolean, default=True)
    
    category = relationship("CategoryModel", uselist=False, back_populates='products')
    shopping_carts = relationship('ShoppingCartModel', uselist=True, back_populates='product')


