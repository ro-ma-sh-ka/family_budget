from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('add_expenses/', add_expenses_view, name='add_expenses'),
    # path('add_expenses/', add_new_expense_view, name='add_new_expense_view'),
    path('show_expenses/', show_expenses_view, name='show_expenses'),
    path('delete_expense/<int:pk>>', delete_expense_view, name='delete_expense'),
    path('update_expense/<int:pk>', update_expense_view, name='update_expense'),
    path('import/', import_past_expenses_view, name='import_past_expenses'),
    ]