from django.db import models
from datetime import datetime
from product.models import Product
from authentication.models import User


class Product_Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pd_review_date = models.DateTimeField(default=datetime.now())
    pd_review_text = models.CharField(max_length=500, default="")

