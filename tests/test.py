import unittest
from flask import current_app
from app import create_app



class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_add_user(self):
        response = self.client.post('/api/v1/register', json={'username':'john'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('message',response.get_json())

    def test_coins_endpoint(self):
        # Mock JWT authentication for testing
        response = self.client.post('/api/v1/login', json={'username': 'john'})
        token = response.get_json()['token']

        # Use the token to access the protected endpoint
        response = self.client.get('/api/v1/coins', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code in [200, 308], True)

    def test_categories_endpoint(self):
        # Mock JWT authentication for testing
        response = self.client.post('/api/v1/login', json={'username': 'john'})
        token = response.get_json()['token']

        # Use the token to access the protected endpoint
        response = self.client.get('/api/v1/categories', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code in [200, 308],True)

    def test_valid_login(self):
        response = self.client.post('/api/v1/login', json={'username': 'john'})
        print(response.get_json())
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

if __name__ == '__main__':
    unittest.main()
