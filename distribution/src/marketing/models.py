from django.db import models

# Create your models here.

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.TimeField(auto_now_add=True)
