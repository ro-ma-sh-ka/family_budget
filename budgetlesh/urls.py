"""budgetlesh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

import accounts.views
from budgetdb.views import startpage_view, add_past_expenses_view, show_expenses_view, add_new_expense_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', startpage_view, name='startpage_view'),
    path('add_expenses/', add_new_expense_view, name='add_new_expense_view'),
    path('show_expenses/', show_expenses_view, name='show_expenses_view'),
    path('import/', add_past_expenses_view, name='add_past_expenses_view'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/new_account/', accounts.views.new_account_view, name='new_account'),
]
