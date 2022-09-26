from flask_restx import fields


class MercadoPagoRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Mercadopago User Test Create', {
            'description': fields.String(required=True)
        })

