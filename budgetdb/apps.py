from datetime import datetime
from django.apps import AppConfig


class BudgetdbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'budgetdb'


class DateConverter:
    '''
    The Converter to adjust date format from csv file to DB format and back when we import or export past expenses
    regex - date format we must receive from csv file
    db_date_format - current DB format
    excel_date_format - current excel format we use
    '''

    # regex = '{0-9}{4}-{0-9}{2}-{0-9}{2}'
    db_date_format = '%Y-%m-%d'
    excel_date_format = '%d.%m.%Y'

    def to_db_format(self, excel_date: str) -> datetime:
        return datetime.strptime(excel_date, self.excel_date_format)

    def to_excel_format(self, db_date: datetime) -> str:
        return db_date.strftime(self.excel_date_format)
