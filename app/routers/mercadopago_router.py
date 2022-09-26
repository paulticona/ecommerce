from app import api
from flask import request
from flask_restx import Resource
from app.schemas.mercadopago_schema import MercadoPagoRequestSchema
from app.utils.mercadopago import Mercadopago

namespace = api.namespace(
    name='Mercadopago',
    description='Endpoints para la integración de mercadopago',
    path='/mercadopago'
)

schema = MercadoPagoRequestSchema(namespace)


@namespace.route('/users/test')
@namespace.doc(security='Bearer')
class UserTest(Resource):
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear un usuario de prueba '''
        util = Mercadopago()
        return util.createUserTest(request.json)

api.add_namespace(namespace)
