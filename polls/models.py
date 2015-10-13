from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    def was_published_recently(self):
    	return self.pub_date >= timezone.now().date() - datetime.timedelta(days=1)
    	was_published_recentlu.admin_order_field = 'pub_date'
    	was_published_recentlu.boolean = True
    	was_published_recentlu.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

