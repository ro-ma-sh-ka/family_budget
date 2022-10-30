from django.shortcuts import render
from django.http import HttpResponse
import csv
from budgetdb.models import Budgettable
import time



def startpage_view(request):
    return render(request, 'base.html')


def importcsv_view():
    with open('budgetlesh.csv', 'r', newline='') as csvfile:
        past_data = csv.reader(csvfile, delimiter=',')
        expenses = []
        for data in past_data:
            data = data[1:5]
            expenses.append(data)
    expenses.pop(0)
    for row in expenses:
        row[0] = time.strptime(row[0], '%d.%m.%Y')
        row[0] = time.strftime('%Y-%m-%d', row[0])
        # Budgettable.objects.create(created_on=datetime.now(), updated_on=datetime.now(), date=row[0], total=row[1], what_is=row[2], section=row[3])
    return HttpResponse(Budgettable.objects.all())


def exportcsv_view():
    pass


def create_view(request):
    return render(request, 'register.html')


def checkin_view():
    pass
