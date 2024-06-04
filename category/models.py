
from django.db import models
from django.db.models.sql import constants


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150, unique=True,null=False,blank=False)

    def __str__(self):
        return self.category_name
