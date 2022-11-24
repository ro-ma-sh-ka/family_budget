from django.db import models


class Currency(models.Model):
    currency = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.currency


class Section(models.Model):
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.section


class FamilyMembers(models.Model):
    members = models.CharField(max_length=100, default='familyenter')

    def __str__(self):
        return self.members


class Budget(models.Model):
    creator = models.ForeignKey(FamilyMembers, on_delete=models.PROTECT, related_name='creators')
    created_on = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(FamilyMembers, on_delete=models.PROTECT, related_name='editors')
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField()
    total = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    what_is = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk)

    # End of lesson 8
    # https://www.youtube.com/watch?v=CFO4aAsUuUk&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=8&ab_channel=selfedu
    # I'd like to get this function for delete and edit but how to get this function for different view functions???

    # def get_absolute_url(self, view_function):
    #     return reverse(view_function, kwargs={'pk': self.pk})
