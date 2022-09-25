from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.products_model import ProductModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

class ProductsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        parser = RequestParser()
        parser.add_argument('name', type=str, required=True, location='form')
        parser.add_argument('description', type=str, required=True, location='form')
        parser.add_argument('price', type=float, required=True, location='form')
        parser.add_argument('image', type=FileStorage, required=True, location='files')
        parser.add_argument('stock', type=int, required=True, location='form')
        parser.add_argument('category_id', type=int, required=True, location='form')
        
    
        return parser
    def update(self):
        return self.namespace.model('Product Update', {
            'name': fields.String(required=False, min_length=2, max_length=120),

        })


class ProductsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        ordered = True
