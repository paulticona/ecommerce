from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.stores_model import StoreModel


class StoresRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Store Create', {
            'name': fields.String(required=True, min_length=2, max_length=120),
            'address': fields.String(required=True, min_length=2, max_length=255),
            'telephone': fields.Integer(required=True),
            'store_section_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('Store Update', {
            'name': fields.String(required=False, min_length=2, max_length=120),
            'address': fields.String(required=False, min_length=2, max_length=255),
            'telephone': fields.Integer(required=False),
            'store_section_id': fields.Integer(required=False)
        })


class StoresResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = StoreModel
        ordered = True
