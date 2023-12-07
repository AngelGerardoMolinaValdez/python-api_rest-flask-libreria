import sys
import os
import unittest
import base64
from assertpy import assert_that

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', "src")
    )
)

from src.app import create_app

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.credentials = base64.b64encode(b"admin:1234").decode('utf-8')
        self.app = create_app({"TESTING": True}).test_client()

    def test_get_productos(self):
        response = self.app.get(
            '/products',
            headers={"Authorization": f"Basic {self.credentials}"}
        )
        assert_that(response.status_code).is_equal_to(200)

    def test_post_producto(self):
        test_producto = {"name": "Producto 3", "category": "Ropa", "stock": 15}
        response = self.app.post(
            '/products',
            json=test_producto,
            headers={"Authorization": f"Basic {self.credentials}"}
        )
        assert_that(response.status_code).is_equal_to(201)


if __name__ == '__main__':
    unittest.main()
