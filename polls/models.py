# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200) # varchar
    pub_date = models.DateTimeField('date published') # DateTime

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)  # Foreign key constraint
    choice_text = models.CharField(max_length=200) #varchar
    votes = models.IntegerField(default=0)  # int field


    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text


  

