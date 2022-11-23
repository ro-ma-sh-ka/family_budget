from django.db import models
from django.urls import reverse


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

    # End of lesson 8
    # https://www.youtube.com/watch?v=CFO4aAsUuUk&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=8&ab_channel=selfedu
    # I'd like to get this function for delete and edit but how to get this function for different view functions???

    # def get_absolute_url(self, view_function):
    #     return reverse(view_function, kwargs={'pk': self.pk})
