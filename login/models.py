from django.db import models

# Create your models here.

class User(models.Model):
    """
    this class is used to create a user model with username and password
    """
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username