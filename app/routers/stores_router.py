from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.stores_schema import StoresRequestSchema
from app.controllers.stores_controller import StoresController

namespace = api.namespace( 
    name='Stores',
    description='Endpoints para las tiendas',
    path='/stores'
)

request_schema = StoresRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Stores(Resource):
    @jwt_required()
    def get(self):
        '''Listar todas las Tiendas'''
        controller = StoresController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear una Tienda'''
        controller = StoresController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class StoresById(Resource):
    @jwt_required()

    def get(self, id):
        '''Obtener una Tienda por el ID'''
        controller = StoresController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar una Tienda por el ID'''
        controller = StoresController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar una Tienda por el ID'''
        controller = StoresController()
        return controller.delete(id)


api.add_namespace(namespace)
