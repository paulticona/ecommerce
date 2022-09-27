from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class OrderModel(BaseModel):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_price = Column(Float(precision=2))
    subtotal_price = Column(Float(precision=2))
    igv_price = Column(Float(precision=2))
    discount_price = Column(Float(precision=2))
    correlative = Column(String(12))
    checkout_id = Column(String(255), nullable=True)
    checkout_url = Column(String(255), nullable=True)
    payment_status = Column(String, nullable=True)
    payment_detail = Column(String, nullable=True)
    status = Column(String, default='pending')

    items = relationship('OrderItemModel', uselist=True,
                         back_populates='order')
