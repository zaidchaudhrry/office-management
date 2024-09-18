from django.db import models
import uuid

class Product(models.Model):
    productId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    rating = models.FloatField(null=True, blank=True)
    stockQuantity = models.IntegerField()

    def __str__(self):
        return self.name
