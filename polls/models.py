# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200) # varchar
    pub_date = models.DateTimeField('date published') # DateTime


class Choice(models.Model):
    question = models.ForeignKey(Question)  # Foreign key constraint
    choice_text = models.CharField(max_length=200) #varchar
    votes = models.IntegerField(default=0)  # int field
