from django.db import models

# Create your models here.

class credentials(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)