from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from category.models import Category


class Product(models.Model):
    promotion = (('True', "oui"),
                 ('False', "non"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=150, default='')
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(default='')
    thumbnail = models.ImageField(upload_to='media')
    publish = models.DateField(default=datetime.now())
    slug = models.SlugField(max_length=128, unique=True)
    promo = models.CharField(max_length=50, default='False', choices=promotion)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_id': self.id})
