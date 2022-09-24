from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.holidays_model import HolidayModel
from marshmallow import Schema, fields as fields_ms


class HolidaysRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Holiday Create', {
            # año-mes-dias
            'date': fields.Date(required=True, format='%Y-%m-%d'),
            'description': fields.String(required=True, min_length=2, max_length=160)
        })

    def update(self):
        return self.namespace.model('Holiday Update', {
            'date': fields.Date(required=False, format='%Y-%m-%d'),
            'description': fields.String(required=False, min_length=2, max_length=160)
        })


class HolidaysResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HolidayModel
        ordered = True


class HolidaysDeliveryResponseSchema(Schema):
    class Meta:
        ordered = True
    date = fields_ms.Date(format='%Y-%m-%d')
    format = fields_ms.String()

