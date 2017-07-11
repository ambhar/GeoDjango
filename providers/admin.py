# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Provider, Service

admin.site.register(Provider)
admin.site.register(Service)
