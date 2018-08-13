# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator

class TwitterProfile (models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    description  = models.CharField(max_length=400)
    imageURI = models.TextField(validators=[URLValidator()])
    popularityIndex = models.CharField(max_length=400)
    def __str__(self):
		return (self.name)

class Request (models.Model):
    username = models.CharField(max_length=100)
    createdDate = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=100, default= "Pending")

    class Meta:
        get_latest_by = 'createdDate'

    def __str__(self):
		return (self.username)