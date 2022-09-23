from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.categories_schema import CategoriesRequestSchema
from app.controllers.categories_controller import CategoriesController

namespace = api.namespace( 
    name='Categories',
    description='Endpoints para las Categorias',
    path='/Categories'
)

request_schema = CategoriesRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Stores(Resource):
    @jwt_required()
    def get(self):
        '''Listar todas las Categoría'''
        controller = CategoriesController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear una Categoría'''
        controller = CategoriesController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class StoresById(Resource):
    @jwt_required()

    def get(self, id):
        '''Obtener una Categoría por el ID'''
        controller = CategoriesController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar una Categoría por el ID'''
        controller = CategoriesController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar una Categoría por el ID'''
        controller = CategoriesController()
        return controller.delete(id)


api.add_namespace(namespace)
