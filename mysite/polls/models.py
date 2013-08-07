from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		'''
		for human readable model representation 
		'''
		return self.question

	def was_published_recently(self):
		'''
		easy method for returning published polls with in 1 day
		'''
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		'''
		for human readable model representation 
		'''
		return self.choice_text
