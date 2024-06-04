from django.db import models
from django.forms import ModelForm


# Create your models here.

class Email(models.Model):
    email_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    destination = models.EmailField()
    message = models.TextField(max_length=2000)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email_name}-{self.subject}-{self.date_sent}"

