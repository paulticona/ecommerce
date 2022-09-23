from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.products_model import ProductModel


class ProductsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Product Create', {
            'name': fields.String(required=True, min_length=2, max_length=120),
            'description': fields.String(required=True, min_length=2, max_length=255),
            'price': fields.Float(required=True),
            'image': fields.String(required=True),
            'stock': fields.Integer(required=True),
        })

    def update(self):
        return self.namespace.model('Product Update', {
            'name': fields.String(required=False, min_length=2, max_length=120),
            'description': fields.String(required=True, min_length=2, max_length=255),
            'price': fields.Float(required=True),
            'image': fields.String(required=True),
            'stock': fields.Integer(required=True),
        })


class ProductsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        ordered = True
