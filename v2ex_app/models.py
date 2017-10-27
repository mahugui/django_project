# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from scrapy_djangoitem import DjangoItem
# Create your models here.


class DataModel(models.Model):
    title = models.CharField(max_length=2048)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    reply_count = models.CharField(max_length=2014)
    url = models.CharField(max_length=1024)
    base_url = models.CharField(max_length=1024)
    node = models.CharField(max_length=255)

    class Meta:
        db_table = "v2ex"

    def __unicode__(self):
        return u"name: {}| title: {}".format(self.name, self.title)


class DataItem(DjangoItem):
    django_model = DataModel