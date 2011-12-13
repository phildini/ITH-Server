from django.db import models
from django.contrib.auth.models import User
from choices import *


class Team(models.Model):
    # ******************
    members=models.ManyToManyField(User)
    #owner=models.ForeignKey(User)
    # *************
    team_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    project_type = models.CharField(max_length=1, choices=PROJ_CHOICES)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=1, choices=STATE_CHOICES)

    def __unicode__(self):
        return self.team_name


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    project_type = models.CharField(max_length=1, choices=PROJ_CHOICES)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)

    def __unicode__(self):
        return self.project_name
