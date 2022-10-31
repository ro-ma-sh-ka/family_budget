from django.db import models


class Budgettable(models.Model):
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    date = models.DateField()
    total = models.FloatField()
    currency = models.CharField(max_length=10)
    what_is = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
