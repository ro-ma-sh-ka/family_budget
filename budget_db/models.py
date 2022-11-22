from django.db import models


class Budget(models.Model):
    creator = models.CharField(max_length=100, default='familyenter')
    created_on = models.DateTimeField(auto_now_add=True)
    updater = models.CharField(max_length=100, default='familyenter')
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField()
    total = models.FloatField()
    currency = models.CharField(max_length=10)
    what_is = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
