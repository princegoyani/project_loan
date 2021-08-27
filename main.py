from os import error, read
import pandas as pd

import math
import datetime
from dateutil.relativedelta import relativedelta
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def due_Date_cal(due_date_ini, Starting_date):
    Starting_date = datetime.date.fromisoformat(str(Starting_date))

    due_date_ini = datetime.date.fromisoformat(str(due_date_ini))

    if datetime.date.today() > due_date_ini:
        due_months = (datetime.date.today().year - due_date_ini.year) * \
            12 + (datetime.date.today().month - due_date_ini.month) + 1

    else:
        due_months = 0

    #due_date = due_date_ini + relativedelta(months=due_months)

    return due_months

   # paid_amount = loan_amount - (bal_amount+emi)
   # print(paid_amount)
    # no_oftimepaid = paid_amount / emi
    # print(no_oftimepaid)
    # mon = no_oftimepaid + 1
    # print(mon)

    # print(Starting_date)
    # print(type(Starting_date))


""" if Starting_date == "0":
        print("LOAN IS WAITING")
        due_Date = "0"
    else:
        Start_dateformat = datetime.date.fromisoformat(str(Starting_date))
    # print(Start_dateformat.year)
        due_Date = Start_dateformat + relativedelta(months=no_oftrans)
"""


def due_amount_cal(due_date, emi, due_amount_ini):

    if str(due_date) == "0":
        print("LOAN IS WAITING")
        due_amount = 0

    #due_months = due_Date_cal()

    else:
        due_date = datetime.date.fromisoformat(str(due_date))
        if datetime.date.today() > due_date:
            due_months = (datetime.date.today().year - due_date.year) * \
                12 + (datetime.date.today().month -
                      due_date.month)  # +1 as before it return months difference between due date and today but a month before due date also need to included

            # due amount are punishment so it not just adding emi also the amount before a month
            due_amount = emi * (due_months+1)
            # print(due_months)
        else:
            due_amount = due_amount_ini

    return due_amount


def Check_loan():             # checking loan_data
    client_data = pd.read_csv("Client Database.csv",
                              sep=",", header=0)

    for i in client_data.index:
        balance_out = client_data.loc[i, "Balance_out"]
        # print("BAL_OUT", balance_out <= 0)
        if balance_out <= 0 and "open" == client_data.loc[i, "Status"].lower():
            client_data.loc[i, "Status"] = "expired"

    client_data.to_csv("Client Database.csv", index=False)


def monthly_pay_int(loan_amount, time, int_rates):      # emi calculater
    # print(loan_amount, time, int_rates)
    # print()

    no_ofmonths = time * 12  # year in month
    # int_rate out of persent and / 12 bcz we want monthly
    month_intreset = int_rates / 100 / 12
   # #print(no_ofmonths)

    # print("Montly Intreset :", month_intreset * 100)

    a = math.pow((1 + month_intreset), no_ofmonths)
   # #print("A : ", a)
    b = a - 1
    month_payment = loan_amount * month_intreset * a/b
    # rou_moth_pay = round(month_payment)
    # print("Your Montly Payment Will be : ", rou_moth_pay)

    return month_payment  # , rou_moth_pay

# pay now


"""
def due_Date_cal(Loan_amount, bal_out, emi, no_oftrans, Starting_date):
  #  paid_amount = Loan_amount - bal_out
  #  no_oftimepaid = paid_amount / emi
  #  mon = no_oftimepaid + 1
   # #print(mon)
    # #print(type(Starting_date))
    Start_dateformat = datetime.date.fromisoformat(Starting_date)
    # print(Start_dateformat.year)
    due_Date = Start_dateformat + relativedelta(months=no_oftrans + 1)
    return due_Date
"""


# of employ to get all client info


def move_tomainmenu(inp, menu):
    if menu == "client":
        con_menu = "Main_Menu"
    elif menu == "emp":
        con_menu = "emp_main_menu"

    if inp.lower() == "q":
        while True:
            confirm = input(
                "Are you sure you want to go to MAIN MENU (YES/NO):")
            if confirm.lower() == "yes" or confirm.lower() == "y":
                raise ChildProcessError

            elif confirm.lower() == "no" or confirm.lower() == "n":
                break

            else:
                print("\nTRY AGAIN !")
                continue
        # print(error)


def get_data_status(client_data, status):

    client_datas_ofstatus = pd.DataFrame(columns=client_data.columns)
    row = 1
    # print(client_data.index)
    for i in client_data.index:
        if client_data.loc[i, "Status"].lower() == status:
            client_datas_ofstatus.loc[row] = client_data.loc[i, :]
            row = row + 1

    return client_datas_ofstatus
    # print(client_datas_ofstatus)


def client_loans(client_data, clientid, Status):  # for client to get there loan_info

    client_loan_data = pd.DataFrame(
        columns=["Loan_id", "Loan", "Rate", "Total Principal", "Total Interest", "Loan_Amount", "Time", "Bal_Out", "EMI", "Due_date", "Due_amount", "NO_ofPayment", "Start_Date", "Status"])
    # print(client_loan_data)
    # print(client_data)
    # print(clientid in client_data["Client ID"].tolist())
    # and "open" == client_data["Status"]():
#    if clientid in client_data["Client ID"].tolist():
    if type(Status) == list:
        Status = Status
    else:
        Status = [Status]

    # print("STATUS", Status)

    i = 1
    for index1 in client_data["Client ID"].index:

        # print("STATUS", Status == client_data.loc[index1, "Status"])
        # print(client_data.loc[index1, "Status"])
        # print("CLIENT ", clientid == client_data.loc[index1, "Client ID"])
        if clientid == client_data.loc[index1, "Client ID"] and client_data.loc[index1, "Status"].lower() in Status:
            loan_id = client_data.loc[index1, "loan_id"]
            typeofloan = client_data.loc[index1, "Types of Loans"]
            loan_amount = client_data.loc[index1, "Loan_amount"]
            rate = client_data.loc[index1, "Rate of Intrest"]
            principal = client_data.loc[index1, "Loan_amount"]
            san_amount = client_data.loc[index1, "Sanctioned Amount"]
            time = client_data.loc[index1, "for YEAR"]
            balance_out = client_data.loc[index1, "Balance_out"]
            emi = client_data.loc[index1, "EMI"]
            principal = client_data.loc[index1, "Total_Principal"]
            interest = client_data.loc[index1, "Total_Interest"]
            no_oftrans = client_data.loc[index1, "No_ofTransaction"]
            starting_date = client_data.loc[index1, "Starting_date"]
            due_date_ini = client_data.loc[index1, "Due_date"]
            due_amount_ini = client_data.loc[index1, "Due_amount"]
            status_client = client_data.loc[index1, "Status"]
            # print(due_date_ini)
            # print(starting_date)
            """if due_amount_ini == 0:
                due_amount = 0
            else:
                """
            if status_client != "open":
                due_date = 0
                due_amount = 0
            # print("Starting ", starting_date)
     #       due_date = due_Date_cal(no_oftrans, starting_date)
            else:
                due_date = due_date_ini
                due_amount = due_amount_cal(due_date, emi, due_amount_ini)
                # print(due_date)
            client_loan_data.loc[i] = [loan_id, typeofloan, rate,
                                       principal, interest, loan_amount, time, balance_out, emi, due_date, due_amount, no_oftrans, starting_date, status_client]

            i = i + 1

        # print(len(client_loan_data))
    """if len(client_loan_data) == 0:
        print("NO LOAN AMOUNT OUT STANDING")
    """
    return client_loan_data

    """
            # print("WELCOME")
            client_index = index
            # print(client_index)
            pay(client_data, client_index)
            break
        """


"""    else:
        # print("NO LOAN AMOUNT OUT STANDING")
        quit()
"""
#    else:
#       #print("NO LOAN AMOUNT OUT STANDING")


def transaction(client_id):

    trans_data = pd.read_csv("Transaction_Database.csv")

    trans_hist = pd.DataFrame(columns=trans_data.columns)
    trans_amount = 0
    for index in trans_data.index:

        last_index = len(trans_hist.index)
        if client_id == trans_data.loc[index, "Client ID"]:
            trans_hist.loc[last_index] = trans_data.loc[index, :]
            trans_amount = trans_amount + \
                trans_hist.loc[last_index, "Transaction_Amount"]
          #  last_index = len(trans_data.index)

    return trans_hist, trans_amount


def bal_calculater(loan_amount, rate, time, months):

    rate_formated = rate / 100 / 12
   # months = time * 12
  #  print(months)
  #  print(emi)
    a = math.pow((1 + rate_formated), time * 12)
    b = a - 1
    bal_amount = loan_amount * (a - math.pow((1 + rate_formated), months)) / b
    # print(bal_amount)

    return bal_amount
