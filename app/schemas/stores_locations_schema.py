from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.stores_locations_model import StoreLocationModel


class StoresLocationsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Store Locations Create', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })

    def update(self):
        return self.namespace.model('Store Locations Update', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })


class StoresLocationsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = StoreLocationModel
        ordered = True
