from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.coupons_model import CouponModel
from datetime import datetime


class CouponsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Coupon Create', {
            'code': fields.String(required=True, min_length=1, max_length=50),
            'procentage': fields.Float(required=True, precision=2),
            'started_ad': fields.String(required=True, default='YYYY-MM-DD HH:mm:ss'),
            'ended_ad': fields.String(required=True, default='YYYY-MM-DD HH:mm:ss')
        })

    def update(self):
        return self.namespace.model('Coupon Update', {
            'code': fields.String(required=False, min_length=1, max_length=50),
            'procentage': fields.Float(required=False, precision=2),
            'started_ad': fields.String(required=False, default='YYYY-MM-DD HH:mm:ss'),
            'ended_ad': fields.String(required=False, default='YYYY-MM-DD HH:mm:ss')
        })


class CouponsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CouponModel
        ordered = True
