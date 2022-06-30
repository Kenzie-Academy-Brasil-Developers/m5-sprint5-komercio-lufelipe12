from django.test import TestCase

from ..models import Product
from users.models import User


class ProductRelationTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user = User.objects.create(
            email="tia@g.com",
            password="1234",
            first_name="Dona Florinda",
            last_name="Girafales",
            is_seller=True,
        )

        cls.products = [
            Product.objects.create(
                description="Daora",
                price=10.0,
                quantity=1,
                is_active=True,
                seller_id=1,
            )
            for _ in range(3)
        ]

    def test_user_may_contain_products_films(self):

        self.assertEquals(len(self.products), self.user.products.count())

    def test_product_cannot_belong_to_more_than_one_user(self):

        user_two = User.objects.create(
            email="tiazinha@g.com",
            password="1234",
            first_name="Mila",
            last_name="Girafales",
            is_seller=True,
        )

        for product in self.products:
            product.seller_id = user_two.id
            product.save()

        for product in self.products:
            self.assertNotIn(product, self.user.products.all())
            self.assertIn(product, user_two.products.all())
