# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
import west.views

urlpatterns = [
	url(r'^$', west.views.west_index),
	url(r'^staff/', west.views.staff),
	]