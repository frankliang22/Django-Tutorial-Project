from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    def was_published_recently(self):
        yesterday = timezone.now().date() - datetime.timedelta(days=1)
    	return self.pub_date <= yesterday

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

