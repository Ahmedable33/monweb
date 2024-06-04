from django.db import models

from command.models import Command
from products.models import Product

from django.urls import reverse


# Create your models here.


class CommandDetail(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
