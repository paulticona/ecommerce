from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.holidays_schema import HolidaysRequestSchema
from app.controllers.holidays_controller import HolidaysController

namespace = api.namespace(
    name='Feriados',
    description='Endpoints para las Holidays',
    path='/feriados'
)

request_schema = HolidaysRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Holidays(Resource):
    @jwt_required()
    def get(self):
        '''Listar todos los Feriados'''
        controller = HolidaysController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear un Feriado'''
        controller = HolidaysController()
        return controller.create(request.json)


@namespace.route('/delivery_dates')
@namespace.doc(security='Bearer')
class HolidaysDeliveryDates(Resource):
    @jwt_required()
    def get(self):
        '''Listar todos los dias de Entrega'''
        controller = HolidaysController()
        return controller.deliveryDates()


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class HolidaysById(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener un Feriado por el ID'''
        controller = HolidaysController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar un Feriado por el ID'''
        controller = HolidaysController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar un Feriado por el ID'''
        controller = HolidaysController()
        return controller.delete(id)


api.add_namespace(namespace)
