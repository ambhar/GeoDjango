# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.gis.db import models

# import pycountry


# list of all of the language codes, later we can make use of pycountry library to get list of all languages
LANGUAGE_CHOICES = [
    ('USA','ENGLISH-US'),
    ('UK','ENGLISH-UK'),
    ('Japan','JAPANESE'),
    ('China','MANDARIN'),
    ('France', 'FRENCH'),
    ('Germany','GERMAN'),
    ('Portugal','PORTUGUESE'),
    ('Spain','SPANISH')
]

# list of all of the currency codes, later we can make use of pycountry library to get list of all currencies
CURRENCY_CHOICES = [
    ('Europe','EUR'),
    ('Britain','GBP'),
    ('Japan','JPY'),
    ('USA','USD')
]


# Provider Model
class Provider(models.Model):
    name = models.CharField(max_length=70, null=True, blank=True)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+12394579799'. 9 to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True) # validatong phone numbers
    language = models.CharField(max_length=6, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=6, choices=CURRENCY_CHOICES)

    def save(self, *args, **kwargs):
        if self.email == "":
            raise ValidationError('Please enter email address !')
        super(Provider, self).save(*args, **kwargs)

    def __str__(self):           
        return self.name
    

# Service Model
class Service(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, null=True, blank=True)
    price = models.FloatField(default=0, unique=False)
    polygon = models.PolygonField()

    def __str__(self):           
        return self.name

    class Meta:
        unique_together = ('provider', 'name',)

