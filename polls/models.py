
from django.db import models


class User(models.Model) :
    user_id = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()

class Review(models.Model) :
    author = models.ForeignKey('auth.User')
    overall = models.IntegerField()
    taste = models.IntegerField()
    price = models.IntegerField()
    text = models.CharField(max_length=400)
