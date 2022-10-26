from django.db import models


class budget_table(models.Model):
    # id_note = models.AutoField()
    created_on = models.DateTimeField()
    date = models.DateField()
    total = models.FloatField()
    what_is = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
