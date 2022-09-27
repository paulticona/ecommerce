from os import getenv
from requests import post, get


class Mercadopago:
    def __init__(self):
        self.main_token = getenv('MERCADOPAGO_MAIN_ACCESS_TOKEN')
        self.child_token = getenv('MERCADOPAGO_CHILD_ACCESS_TOKEN')

        self.main_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.main_token}'
        }

        self.child_header = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.child_token}'
        }

        self.base_url = 'https://api.mercadopago.com'
        self.site_id = 'MPE'

    def createUserTest(self, data):
        url = f'{self.base_url}/users/test'
        response = post(
            url,
            json={
                'description': data['description'],
                'site_id': self.site_id
            },
            headers=self.main_headers
        )
        return response.json() or {}

    def allMethodsPaying(self):
        url = f'{self.base_url}/v1/payment_methods'
        response = get(url, headers=self.main_headers)
        return response.json() or {}

    def createPreferences(self, payer, products, order_correlative):
        url = f'{self.base_url}/checkout/preferences'

        # {
        #     'name': 'Roberto',
        #     'surname': 'Quiroga',
        #     'email': 'roberto.quiroga@gmail.com'
        # }

        # {
        #     'id': 1,
        #     'title': 'Producto 1',
        #     'quantity': 2,
        #     'unit_price': 150.20,
        #     'currency_id': 'PEN'
        # }

        body = {
            'back_urls':{
                'success': '',
                'pending': '',
                'failure': ''
            },
            'external_references': order_correlative,
            'payer': payer,
            'items': products 
        }
        response = post(url, json=body, headers=self.child_header)
        return response.json() or {}

