from app.controllers.shopping_carts_controller import ShoppingCartsController
from app.models.orders_model import OrderModel
from app.models.orders_items_model import OrderItemModel
from flask_jwt_extended import current_user


class OrderController:
    def __init__(self):
        self.shopping_cart = ShoppingCartsController()
        self.model = OrderModel
        self.model_item = OrderItemModel
        self.urser_id = current_user['id']

    def create(self):
        try:
            shopping_cart = self.shopping_cart._getAllItems()
            prices = shopping_cart['prices']

            order = self.model.create(
                user_id=self.urser_id,
                total_price=prices['total'],
                subtotal_price=prices['subtotal'],
                igv_price=prices['igv'],
                discount_price=0.00,
                correlative=''
            )
            # __dict__  es para acceder a todos sus objets
            print(order.__dict__)

            return {}, 200
        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e),
            }, 500
