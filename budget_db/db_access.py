from budget_db.models import Budget
import traceback


def add_expenses(created_on, creator, updated_on, updater, date, total, currency, what_is, section):
    try:
        new_expenses = Budget()
        new_expenses.created_on = created_on
        new_expenses.creator = creator
        new_expenses.updated_on = updated_on
        new_expenses.updater = updater
        new_expenses.date = date
        new_expenses.total = total
        new_expenses.currency = currency
        new_expenses.what_is = what_is
        new_expenses.section = section
        new_expenses.save()
    except Exception:
        return traceback.print_exc()
