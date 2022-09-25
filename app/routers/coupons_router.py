from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.coupons_schema import CouponsRequestSchema
from app.controllers.coupons_controller import CouponsController

namespace = api.namespace(
    name='Cupones',
    description='Endpoints para las Cupones',
    path='/coupons'
)

request_schema = CouponsRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Coupons(Resource):
    @jwt_required()
    def get(self):
        '''Listar todos los Cupones'''
        controller = CouponsController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear un Cupon'''
        controller = CouponsController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class CouponsById(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener un Cupon por el ID'''
        controller = CouponsController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar un Cupon por el ID'''
        controller = CouponsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar un Cupon por el ID'''
        controller = CouponsController()
        return controller.delete(id)


api.add_namespace(namespace)
