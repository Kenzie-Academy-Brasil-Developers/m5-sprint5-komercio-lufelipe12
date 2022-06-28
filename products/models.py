from django.db import models

# Create your models here.


class Product(models.Model):
    description = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField()

    seller = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
