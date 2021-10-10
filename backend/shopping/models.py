from django.db import models

# Create your models here.
class ShoppingItem(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.PositiveSmallIntegerField()
    checked = models.NullBooleanField(default=False)