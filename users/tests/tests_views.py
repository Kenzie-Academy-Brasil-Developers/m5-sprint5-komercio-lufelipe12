from rest_framework.test import APITestCase
from users.models import User


class UsersViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.email = "lf1@g.com"
        cls.password = "1234"
        cls.first_name = "Luiz"
        cls.last_name = "Felipe"
        cls.is_seller = True

        cls.user_seller = {
            "email": "joge@g.com",
            "password": "1234",
            "first_name": "Jorge",
            "last_name": "Lafon",
            "is_seller": True,
        }

        cls.user_buyer = User.objects.create(
            email=cls.email,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=cls.is_seller,
        )

    def test_post_a_seller(self):

        user_1 = {
            "email": "joge@g.com",
            "password": "1234",
            "first_name": "Jorge",
            "last_name": "Lafon",
            "is_seller": True,
        }

        response = self.client.post("/api/accounts/", data=user_1)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data["is_seller"])

    def test_post_a_buyer(self):

        user_1 = {
            "email": "lf@g.com",
            "password": "1234",
            "first_name": "Luiz",
            "last_name": "Felipe",
            "is_seller": False,
        }

        response = self.client.post("/api/accounts/", data=user_1)

        self.assertEqual(response.status_code, 201)
        self.assertFalse(response.data["is_seller"])

    def test_post_a_wrong_data(self):

        user_1 = {
            "email": "lf@g.com",
            "password": "1234",
            "last_name": "Felipe",
            "is_seller": False,
        }

        response = self.client.post("/api/accounts/", data=user_1)

        self.assertEqual(response.status_code, 400)

    def test_login(self):

        self.client.post("/api/accounts/", self.user_seller, format="json")

        login_data = {
            "email": self.user_seller["email"],
            "password": self.user_seller["password"],
        }

        response = self.client.post("/api/login/", login_data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["token"])

    def test_get_users(self):

        response = self.client.get("/api/accounts/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
