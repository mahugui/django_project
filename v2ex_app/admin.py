# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.conf.urls import url
from django.contrib import admin
from django.http.response import HttpResponseRedirect
# Register your models here.

from scrapy_project.v2ex.v2ex.spiders.spider import v2exSpider
# from scrapy_project.v2ex import start_scrawl
from .models import DataModel

os.environ.setdefault('SCRAPY_PROJECT',
                      'scrapy_project.v2ex')

class V2EXAdmin(admin.ModelAdmin):
    list_display = ("title", "name", "url", "author",
                    "node", "base_url", "reply_count", "jump")
    list_per_page = 20
    search_fields = ("title", )
    change_list_template = "v2ex/change_list.html"

    def jump(self, obj):
        url = "{}{}".format(obj.base_url.rstrip("/"), obj.url)
        return '<a href="{}" target="_blank">跳转</a>'.format(url)
    jump.allow_tags = True
    jump.short_description = "foo"

    def get_urls(self):
        urls = super(V2EXAdmin, self).get_urls()
        my_urls = [url(r'^scrapy/$', self.start_scrapy, name="scrapy")]
        return my_urls + urls

    def start_scrapy(self, request):
        start_scrawl()
        return HttpResponseRedirect("/admin/v2ex_app/datamodel/")
admin.site.register(DataModel, V2EXAdmin)
