import datetime
import csv
import traceback

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from budget_db.apps import DateConverter
from budget_db.db_access import add_expense
from budget_db.models import Budget


def home_view(request: any) -> render:
    '''
    home page
    Here we create base page with common information.
    - total/current month - done
    - total by sections
    - graphs
    - invitation to add new_expense
    '''
    expenses = Budget.objects.all()
    total = 0
    for expense in expenses:
        total += expense.total
    context = {
        'expenses': total
    }
    return render(request, 'budget_db/base.html', context=context)


def add_expenses_view(request: any) -> render:
    '''

    '''
    return render(request, 'budget_db/add_expenses.html')


def delete_expense_view(request: any, pk: int) -> render:
    expense = Budget.objects.get(id=pk)
    return render(request, 'budget_db/delete_expense.html', {'expense': expense})


def delete_view(request: any) -> redirect:
    expense = Budget()
    expense.pk = request.POST.get('expense_pk')
    expense_to_delete = Budget.objects.get(id=expense.pk)
    expense_to_delete.delete()
    messages.success(request, 'Expense has deleted')
    return redirect('/')


def update_view(request: any) -> redirect:
    # updated_on = DateConverter().to_db_format(str(request.GET.get('expense_date')))
    expense_to_update = Budget.objects.get(id=request.GET.get('expense_pk'))
    expense_to_update.updated_on = datetime.datetime.now()
    # expense_to_update.date = updated_on,
    expense_to_update.total = request.GET.get('expense_sum')
    expense_to_update.currency = request.GET.get('expenses_currency')
    expense_to_update.what_is = request.GET.get('expense_description')
    expense_to_update.section = request.GET.get('expense_section')
    expense_to_update.save()
    messages.success(request, 'Expense has edited')
    return redirect('/')


def update_expense_view(request: any, pk: int) -> render:
    expense = Budget.objects.get(id=pk)
    return render(request, 'budget_db/update_expense.html', {'expense': expense})


def import_past_expenses_view(request):
    return render(request, 'budget_db/import_past_expenses.html')


def import_view(request: any) -> render:
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
            add_expense(datetime.datetime.now(),
                         'familyenter',
                         datetime.datetime.now(),
                         'familyenter',
                         row[0],
                         row[1],
                         row[2],
                         'RUB',
                         row[3]
                         )
            messages.success(request, 'Past expenses has imported')
        except Exception:
            messages.success(request, f'try again {row[0]} {traceback.print_exc()}')
    return redirect('/')


def add_new_expense_view(request: any) -> render:
    add_expense(datetime.datetime.now(),
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
    return render(request, 'budget_db/base.html')


def show_expenses_view(request: any) -> render:
    show_expenses = Budget.objects.all()

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
    return render(request, 'budget_db/show_expenses.html', context)


def export_csv_view():
    pass
