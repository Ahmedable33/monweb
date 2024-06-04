from django.contrib.auth.models import User
from django.db import models

from datetime import datetime

from django.db import models
from django.urls import reverse


# Create your models here.

# class Command(models.Model):
#     Command_stat = (('Pending', 'Pending'),
#                       ('Send', 'Send'),
#                       ('Delivered', 'Delivered'))
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     command_date = models.DateField(default=datetime.today())
#     command_status = models.CharField(max_length=100, choices=Command_stat)
#
#     def __str__(self):
#         return self.user


class Command(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
