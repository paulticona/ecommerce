from app import db
from app.models.shopping_cart_models import ShoppingCartModel
from app.schemas.sopping_carts_schema import ShoppingCartsResponseSchema
from flask_jwt_extended import current_user


class ShoppingCartsController:
    def __init__(self):
        self.model = ShoppingCartModel
        self.schema = ShoppingCartsResponseSchema
        self.user_id = current_user['id']

    def all(self):
        # ! 1:20 del video 25

        try:
            records = self.model.where(
                user_id=self.user_id).order_by('id').all()
            response = self.schema(many=True)
            return {
                'data': response.dump(records)
            }
        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def update(self, data):
        try:
            action = 'creo'
            if record := self.model.where(
                user_id=self.user_id,
                product_id=data['product_id']
            ).first():
                action = 'Actualizó'
                record.update(**data)
            else:
                data['user_id'] = self.user_id
                record = self.model.create(**data)
            db.session.add(record)
            db.session.commit()
            return {
                'message': f' Se {action}  el producto en el carrito'
            }, 200
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def delete(self, id):
        try:
            if record := self.model.where(id=id).first():
                pass

                # if record.status:
                #    record.update()
                #    db.session.add(record)
                #    db.session.commit()
                # return {
                #    'message': 'Se desabilito la Categoría con exito'
               # }

        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500
