from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required, current_user
from app.schemas.sopping_carts_schema import ShoppingCartsRequestSchema
from app.controllers.shopping_carts_controller import ShoppingCartsController

namespace = api.namespace(
    name='Shopping Carts',
    description='Endpoints para traer el carritod e compras',
    path='/shopping_carts'
)

request_schema = ShoppingCartsRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class ShoppingCarts(Resource):
    @jwt_required()
    def get(self):
        '''Listar productos del Carrito'''
        print(current_user)
        controller = ShoppingCartsController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self):
        '''Crear o Actializar Producto del Carrito'''
        controller = ShoppingCartsController()
        return controller.update(request.json)


@namespace.route('/<int:product_id>')
@namespace.doc(security='Bearer')
class ShoppingCartsById(Resource):

    @jwt_required()
    def delete(self, product_id):
        '''Eliminar Producto del Carrito'''
        controller = ShoppingCartsController()
        return controller.delete(product_id)


api.add_namespace(namespace)
