from os import getenv
from requests import post


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
