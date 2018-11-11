# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Testing end-to-end
# dummy entry 
class Entry(models.Model):
    client_name = models.CharField(max_length=1000, null=True)
    volume = models.FloatField(null=True)
    deal_id = models.IntegerField(null=True)
    rank = models.IntegerField(null=True)
    ev = models.IntegerField(null=True)
