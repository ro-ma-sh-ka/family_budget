import datetime
import csv
import traceback

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from budgetdb.apps import DateConverter
from budgetdb.db_access import add_expenses
from budgetdb.models import Budgettable


def startpage_view(request):
    return render(request, 'base.html')


def add_past_expenses_view(request):
    with open('budgetlesh.csv', 'r', newline='') as csvfile:
        past_data = csv.reader(csvfile, delimiter=',')
        past_expenses = []
        for data in past_data:
            data = data[1:5]
            past_expenses.append(data)
    past_expenses.pop(0)
    for row in past_expenses:
        try:
            row[0] = DateConverter().to_db_format(str(row[0]))
            add_expenses(datetime.datetime.now(),
                         'familyenter',
                         datetime.datetime.now(),
                         'familyenter',
                         row[0],
                         row[1],
                         row[2],
                         'RUB',
                         row[3]
                         )
        except Exception:
            context = f'try again {row[0]} {traceback.print_exc()}'
            return render(request, 'message.html', {'filename': context})
    return render(request, 'message.html', {'filename': 'done'})


def add_new_expense_view(request):
    add_expenses(datetime.datetime.now(),
                 User.username,
                 datetime.datetime.now(),
                 User.username,
                 request.GET.get("expenses_date"),
                 request.GET.get("expenses_sum"),
                 request.GET.get("expenses_currency"),
                 request.GET.get("expenses_description"),
                 request.GET.get("expenses_section")
                 )
    messages.success(request, "Done!")
    return render(request, 'base.html')


def show_expenses_view(request):
    show_expenses = Budgettable.objects.all()

    page_number = request.GET.get('page', 1)
    rows_qty = int(request.GET.get('rows', 10))
    paginator = Paginator(show_expenses, rows_qty)
    page_obj = paginator.get_page(page_number)
    total_rows = paginator.num_pages * rows_qty
    context = {
        'total_rows': total_rows,
        'expenses': page_obj,
        'num_pages': paginator.num_pages,
        'page_obj': page_obj
    }
    return render(request, 'show_expenses.html', context)


def exportcsv_view():
    pass
