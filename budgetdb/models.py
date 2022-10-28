from django.db import models


class Budgettable(models.Model):
    # id = models.AutoField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    date = models.DateField()
    total = models.FloatField()
    what_is = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
