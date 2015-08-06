"""
Check that __unicode__ method returns unicode
"""
from django.db import models


class Category(models.Model):
    """Category"""
    name = models.CharField()

    def __unicode__(self):
        return self.id


class Product(models.Model):
    """Product"""
    name = models.CharField(max_length=255)
    price = models.DecimalField()

    def __unicode__(self):
        return self.price
