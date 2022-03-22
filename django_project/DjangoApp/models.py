from django.db import models


class Orders(models.Model):
    item_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()
    stock_available = models.IntegerField()
    date_ordered = models.DateField()