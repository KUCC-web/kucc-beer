import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # ...
    def __str__(self):
        return self.question_text
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class User(models.Model) :
    user_id = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)

class Review(models.Model) :
    star = int



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # ...
    def __str__(self):
        return self.choice_text

