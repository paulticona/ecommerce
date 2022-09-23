from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.products_schema import ProductsRequestSchema
from app.controllers.products_controller import ProductsController

namespace = api.namespace( 
    name='Products',
    description='Endpoints para las Productos',
    path='/products'
)

request_schema = ProductsRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Products(Resource):
    @jwt_required()
    def get(self):
        '''Listar todos los Productos'''
        controller = ProductsController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear un Producto'''
        controller = ProductsController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class ProductsById(Resource):
    @jwt_required()

    def get(self, id):
        '''Obtener un Producto por el ID'''
        controller = ProductsController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar un Producto por el ID'''
        controller = ProductsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar un Producto por el ID'''
        controller = ProductsController()
        return controller.delete(id)


api.add_namespace(namespace)
