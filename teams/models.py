from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	#owner = models.ForeignKey(User)
	team_name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date created')
	genre = models.CharField(max_length=100)
	project_type = models.CharField(max_length=100)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=100)

	def __unicode__(self):
		return self.team_name
