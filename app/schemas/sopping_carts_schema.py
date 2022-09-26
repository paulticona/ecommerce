from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.shopping_cart_models import ShoppingCartModel
from marshmallow.fields import Nested


class ShoppingCartsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def update(self):
        return self.namespace.model('Shopping Carts Update', {
            'product_id': fields.Integer(required=False, min_length=2, max_length=120, min=1),
            'quantity': fields.Integer(required=False, min=1)
        })


class ShoppingCartsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ShoppingCartModel
        ordered = True

    product = Nested('ProductsResponseSchema', many=False)
