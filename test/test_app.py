import flask_testing
import json
from app import app


class TestFlaskApp(flask_testing.TestCase):
    def create_app(self):
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_submit_valid_data(self):
        valid_data = {
            'date': '2024-09-01',
            'periods': 12,
            'amount': 10000,
            'rate': 5
        }

        response = self.client.post('/submit', data=valid_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('01.10.2024', data)
        self.assertIsInstance(data['01.10.2024'], float)

    def test_submit_invalid_data(self):
        invalid_data = {
            'date': '2024-09-01',
            'periods': 0,
            'amount': 10000,
            'rate': 5
        }

        response = self.client.post('/submit', data=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid period')

        invalid_data['periods'] = 12
        invalid_data['amount'] = 5000

        response = self.client.post('/submit', data=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid amount')

        invalid_data['amount'] = 10000
        invalid_data['rate'] = 9

        response = self.client.post('/submit', data=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid rate')
