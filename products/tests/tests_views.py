from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from products.models import Product
from users.models import User


class ProductsViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.product = {
            "description": "Bike Maluca",
            "price": 100.5,
            "quantity": 1,
        }

        cls.wrong_product = {
            "price": 100.5,
            "quantity": 1,
        }

        cls.user_buyer = {
            "email": "lf@g.com",
            "password": "1234",
            "first_name": "Luiz",
            "last_name": "Felipe",
            "is_seller": False,
        }

        cls.user_seller = {
            "email": "joge@g.com",
            "password": "1234",
            "first_name": "Jorge",
            "last_name": "Lafon",
            "is_seller": True,
        }

    def test_seller_creating_product(self):

        self.client.post("/api/accounts/", self.user_seller, format="json")

        login_data = {
            "email": self.user_seller["email"],
            "password": self.user_seller["password"],
        }

        auth = self.client.post("/api/login/", login_data, format="json")

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + auth.data["token"]
        )

        response = self.client.post(
            "/api/products/",
            self.product,
            format="json",
        )

        self.assertEquals(response.status_code, 201)
        self.assertTrue(response.data["seller"])

    def test_seller_creating_product_with_wrong_keys(self):

        self.client.post("/api/accounts/", self.user_seller, format="json")

        login_data = {
            "email": self.user_seller["email"],
            "password": self.user_seller["password"],
        }

        auth = self.client.post("/api/login/", login_data, format="json")

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + auth.data["token"]
        )

        response = self.client.post(
            "/api/products/",
            self.wrong_product,
            format="json",
        )

        self.assertEquals(response.status_code, 400)
        self.assertTrue(response.data["description"])


    def test_buyer_creating_product(self):

        self.client.post("/api/accounts/", self.user_buyer, format="json")

        login_data = {
            "email": self.user_buyer["email"],
            "password": self.user_buyer["password"],
        }

        auth = self.client.post("/api/login/", login_data, format="json")

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + auth.data["token"]
        )

        response = self.client.post(
            "/api/products/",
            self.product,
            format="json",
        )

        self.assertEquals(response.status_code, 403)
        self.assertEqual(
            response.data,
            {"detail": "You do not have permission to perform this action."},
        )

    def test_list_products(self):

        response = self.client.get("/api/products/")
        self.assertEquals(response.status_code, 200)
