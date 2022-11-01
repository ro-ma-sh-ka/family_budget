import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
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


def add_expenses_view(request):
    new_expenses = Budgettable()
    new_expenses.created_on = datetime.datetime.now()
    new_expenses.updated_on = datetime.datetime.now()
    new_expenses.date = request.GET.get("expenses_date")
    new_expenses.total = request.GET.get("expenses_sum")
    new_expenses.currency = request.GET.get("expenses_currency")
    new_expenses.what_is = request.GET.get("expenses_description")
    new_expenses.section = request.GET.get("expenses_section")
    new_expenses.save()
    messages.success(request, "Done!")
    return render(request, 'base.html')


def show_expenses_view(request):
    show_expenses = Budgettable.objects.all()
    return render(request, 'show_expenses.html', {'expenses': show_expenses})

def exportcsv_view():
    pass