from django.test import TestCase
import datetime
from .models import Question
from django.utils import timezone

class QuestionMethodTests(TestCase):
	
	def test_was_published_recently_with_future_question(self):
		time = timezone.now().date() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently,False)
	
	