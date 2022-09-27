from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.controllers.orders_controller import OrderController

namespace = api.namespace(
    name='orders',
    description='Endpoints para Ordenes - Pedidos',
    path='/orders'
)


@namespace.route('')
@namespace.doc(security='Bearer')
class Orders(Resource):
    @jwt_required()
    def post(self):
        '''Crear Pedido'''
        controller = OrderController()
        return controller.create()