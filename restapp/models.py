# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class stock(models.Model):
    ticker=models.CharField(max_length=10)
    op=models.FloatField()
    cl=models.FloatField()
    vloume=models.IntegerField()

    def __str__(self):

            return self.ticker
