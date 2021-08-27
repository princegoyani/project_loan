from os import error, read
import pandas as pd
import os
from login import clientid
import random
import math
import datetime
from dateutil.relativedelta import relativedelta
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def main_menu():
    a = 0
    while a == 0:
        Check_loan()
        try:
            notics()
            print("PRESS 'q' TO RETURN TO MAIN MENU ANYWHERE IN THE PROGRAM !")
            print("*******************************")
            print("* 1.NEW LOAN                  *\n* 2.NO OF LOAN IS             *\n* 3.PREVIOUS TRANSACTION      *\n* 4.PAY YOUR CURRENT LOAN     *\n* 5.PAYMENT SCHEDULE FOR LOAN *\n* 6)LOGOUT                    *")
            print("*******************************")
            ch = int(input("ENTER YOUR CHOICE:"))

            if ch == 1:

                print("NEW LOAN IS LOADING")
                # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
                new_loan()
                continue
            elif ch == 2:
                print("NO OF LOANS IS")
                # os.system("no_of_loans.py")
                no_of_loans()
                continue
            elif ch == 3:
                print("YOUR PREVIOUS TRANSACTION IS ")

                # exec(open("transaction_history.py").read())
                trans = transaction(clientid)
                trans_hist = trans[0]
                trans_am = trans[1]

                if len(trans_hist) == 0:
                    print("NO PAYMENT TILL !!!")
                else:
                    print(trans_hist)
                    print("YOUR TOTAL NO. OF PAID AMOUNT IS : ", trans_am)

                continue
            elif ch == 4:

                print("Pay Now !")
                pay_now()
                continue

            elif ch == 5:
                print("PAYMENT SCHEDULE")
                pay_shcd()
                continue
            elif ch == 6:
                print("LOGING OUT .....")
                print("Thank you For Visting !")
                # KeyError
                raise ZeroDivisionError

            else:
                print("PLZ REENTER YOUR CHOICE !!!")
                continue
        except ZeroDivisionError:
            print("LOG OUT !")
            os.abort()
            break

        except ValueError:
            print("INVALID !!!")
            print(" IF ANY PROMBLEM PLEASE CONTACT BANK !!! ")
            continue


def pay_now():
    try:
        exec(open("pay_now.py").read())
    except KeyboardInterrupt:
        pass


def new_loan():
    try:
        exec(open("new_loan.py").read())
    except KeyboardInterrupt:
        print("MAIN MENU ")


def pay_shcd():
    try:
        exec(open("pay_shcd.py").read())
    except KeyboardInterrupt:
        pass


def no_of_loans():

    from main import client_loans, move_tomainmenu, Check_loan

    print("1.ALL LOANS \n\n2.CURRENT LOAN \n\n3.WAITING LOAN \n\n4.EXPIRE LOAN")
    while True:

        ch = input("ENTER YOUR CHOICE:")
        move_tomainmenu(ch, "client")
        if ch == '1':
            status_client = ["open", "waiting", "expired"]

        elif ch == '2':
            status_client = ["open"]

        elif ch == '3':
            status_client = ["waiting"]

        elif ch == '4':
            status_client = ["expired"]

        else:
            print("PLEASE RE ENTER YOUR CHOICE")
            continue
        break

    Check_loan()
    client_data = pd.read_csv("Client Database.csv",
                              sep=",", header=0)

    client_loan = client_loans(client_data, clientid, status_client)
    if len(client_loan) == 0:
        print("NO LOAN AMOUNT OUT STANDING")
    else:
        print(client_loan)


def notics():

    Check_loan()

    client_data = pd.read_csv("Client Database.csv",
                              sep=",", header=0)

    client_loan = client_loans(client_data, clientid, "open")
    # print(len(client_loan))
    client_loan_data = client_loan

    today = datetime.date.today()
    loan_ids = []
    total_due = 0
    # a = input()
    for i in client_loan_data.index:
        due_Date = client_loan_data.loc[i, "Due_date"]

        # print("due date", due_Date)
        if due_Date == "0":
            continue
        due_Date = datetime.date.fromisoformat(due_Date)
        if today > due_Date:
            loan_ids.append(client_loan_data.loc[i, "Loan_id"])
            total_due = total_due + client_loan_data.loc[i, "Due_amount"]
            print(
                "*******************************************************************************")
            print(
                f"NOTE !!!! DUE DATE MISSED FOR LOAN {loan_ids}  ! DUE AMOUNT IS {total_due} !!!    *")
            print(
                "*******************************************************************************")
        elif today == due_Date:
            loan_ids.append(client_loan_data.loc[i, "Loan_id"])
            total_due = total_due + client_loan_data.loc[i, "Due_amount"]
            print(
                "*******************************************************************************")
            print(
                f"NOTE !!!!! DUE DATE FOR LOAN {loan_ids} IS TODAY ! DUE AMOUNT IS {total_due} !!!    *")
            print(
                "*******************************************************************************")
        elif today >= due_Date - relativedelta(days=10):
            loan_ids.append(client_loan_data.loc[i, "Loan_id"])
            print(
                "*******************************************************************************")
            print(
                f"NOTE !!!!!!!! DUE DATE FOR LOAN {loan_ids} IS NEAR ! DUE DATE IS {due_Date} !!!    *")
            print(
                "*******************************************************************************")
        else:
            pass


def due_Date_cal(due_date_ini, Starting_date):
    Starting_date = datetime.date.fromisoformat(str(Starting_date))

    due_date_ini = datetime.date.fromisoformat(str(due_date_ini))

    if datetime.date.today() > due_date_ini:
        due_months = (datetime.date.today().year - due_date_ini.year) * \
            12 + (datetime.date.today().month - due_date_ini.month) + \
            1  # due date is a date before a month must be paid

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
            print(due_months)
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
            client_data.loc[i, "Balance_out"] = 0
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
                raise KeyboardInterrupt

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

    # print(client_datas_ofstatus)
    return client_datas_ofstatus


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
                                       round(principal), round(interest), loan_amount, time, round(balance_out), round(emi), due_date, due_amount, no_oftrans, starting_date, status_client]

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


main_menu()
