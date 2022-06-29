from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.email = "joge@g.com"
        cls.password = "1234"
        cls.first_name = "Jorge"
        cls.last_name = "Lafon"
        cls.is_seller = False

        cls.user = User.objects.create(
            email=cls.email,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=cls.is_seller,
        )

    def test_user_has_information_fields(self):
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user.password, self.password)
        self.assertEqual(self.user.first_name, self.first_name)
        self.assertEqual(self.user.last_name, self.last_name)
        self.assertEqual(self.user.is_seller, self.is_seller)
