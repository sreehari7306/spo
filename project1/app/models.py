from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)  # Ensure that this is hashed in the views

    def __str__(self):
        return self.username

