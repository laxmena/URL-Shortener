# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class URLs(models.Model):
	shrinkedURL = models.CharField(max_length=8,primary_key=True)
	targetURL = models.CharField(max_length=2083)
	created = models.DateTimeField(auto_now_add=True, blank=True)