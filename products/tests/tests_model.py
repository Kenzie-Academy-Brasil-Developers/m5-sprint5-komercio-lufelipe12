from django.test import TestCase

from ..models import Product
from users.models import User


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.email = "joge@g.com"
        cls.password = "1234"
        cls.first_name = "Jorge"
        cls.last_name = "Lafon"
        cls.is_seller = True

        cls.user = User.objects.create(
            email=cls.email,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=cls.is_seller,
        )

        cls.description = "Produto massa"
        cls.price = 10.5
        cls.quantity = 2
        cls.is_active = True
        cls.seller_id = 1

        cls.product = Product.objects.create(
            description=cls.description,
            price=cls.price,
            quantity=cls.quantity,
            is_active=cls.is_active,
            seller_id=cls.seller_id,
        )

    def test_product_has_information_fields(self):
        self.assertEqual(self.product.description, self.description)
        self.assertEqual(self.product.price, self.price)
        self.assertEqual(self.product.quantity, self.quantity)
        self.assertEqual(self.product.seller_id, self.seller_id)
        self.assertTrue(self.product.is_active)
