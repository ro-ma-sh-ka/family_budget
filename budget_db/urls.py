from django.urls import path
from .views import *

urlpatterns = [
    path('', start_page_view, name='start_page_view'),
    path('add_expenses/', add_new_expense_view, name='add_new_expense_view'),
    path('show_expenses/', show_expenses_view, name='show_expenses_view'),
    path('import/', add_past_expenses_view, name='add_past_expenses_view'),
    ]