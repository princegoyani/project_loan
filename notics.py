import pandas as pd
import datetime
from login import clientid
from dateutil.relativedelta import relativedelta
from main import due_Date_cal, due_amount_cal, client_loans

client_data = pd.read_csv("Client Database.csv",
                          sep=",", header=0)

client_loan = client_loans(client_data, clientid, "open")
# print(len(client_loan))
client_loan_data = client_loan

today = datetime.date.today()
loan_ids = []
total_due = 0
#a = input()
for i in client_loan_data.index:
    due_Date = client_loan_data.loc[i, "Due_date"]
    #print("due date", due_Date)
    if due_Date == "0":
        continue

    if today > due_Date:
        loan_ids.append(client_loan_data.loc[i, "Loan_id"])
        total_due = total_due + client_loan_data.loc[i, "Due_amount"]
        print("*******************************************************************************")
        print(
            f"NOTE !!!! DUE DATE MISSED FOR LOAN {loan_ids}  ! DUE AMOUNT IS {total_due} !!!    *")
        print("*******************************************************************************")
    elif today == due_Date:
        loan_ids.append(client_loan_data.loc[i, "Loan_id"])
        total_due = total_due + client_loan_data.loc[i, "Due_amount"]
        print("*******************************************************************************")
        print(
            f"NOTE !!!!! DUE DATE FOR LOAN {loan_ids} IS GONE ! DUE AMOUNT IS {total_due} !!!    *")
        print("*******************************************************************************")
    elif today >= due_Date - relativedelta(days=10):
        loan_ids.append(client_loan_data.loc[i, "Loan_id"])
        print("*******************************************************************************")
        print(
            f"NOTE !!!!!!!! DUE DATE FOR LOAN {loan_ids} IS NEAR ! DUE DATE IS {due_Date} !!!    *")
        print("*******************************************************************************")
    else:
        pass


# due date

"""def due_Date_cal(Loan_amount, bal_out, emi, no_oftrans, Starting_date):
  #  paid_amount = Loan_amount - bal_out
  #  no_oftimepaid = paid_amount / emi
  #  mon = no_oftimepaid + 1
   # print(mon)
    # print(type(Starting_date))
    Start_dateformat = datetime.date.fromisoformat(str(Starting_date))
    print(Start_dateformat.year)
    due_Date = Start_dateformat + relativedelta(months=no_oftrans + 1)
    return due_Date
"""
# due amount
"""def due_amount_cal(due_date, emi, bal_out, due_amount_ini):
    if datetime.date.today() > due_date:
        due_months = (datetime.date.today().year - due_date.year) * \
            12 + (datetime.date.today().month - due_date.month)
        print(due_months)
        # due amount are punishment so it not just adding emi also the amount before a month
        due_amount = emi * due_months
    else:
        due_amount = due_amount_ini
    return due_amount
"""
# client_loan
