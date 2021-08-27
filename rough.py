import datetime
from dateutil.relativedelta import relativedelta
due_date_ini = datetime.date.fromisoformat("2021-05-04")
if due_date_ini.day == datetime.date.today().day:
    pass

    if datetime.date.today() > due_date_ini:
        diff = relativedelta(datetime.date.today(), due_date_ini)
        months = diff.years * 12 + diff.months
    """    due_months = (datetime.date.today().year - due_date_ini.year) * \
            12 + (datetime.date.today().month - due_date_ini.month)"""
    print(months)
