import pandas as pd
import math
import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import random
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def number_ofloan_ofaclinet(clientid):

    print("\t\t\t*-----------------*")
    print(
        "\t\t\t| 1.ALL LOANS     |\n\t\t\t| 2.CURRENT LOAN  |\n\t\t\t| 3.WAITING LOAN  |\n\t\t\t| 4.EXPIRE LOAN   |")
    print("\t\t\t*-----------------*")
    while True:
        ch = input("ENTER YOUR CHOICE : ")
        print()
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
    client_data = pd.read_csv("Client Database.csv", sep=",", header=0)
    client_loan = client_loans(client_data, clientid, status_client)
    if len(client_loan) == 0:
        print("NO LOAN AMOUNT OUT OF SELECTED TYPE !")
        print()
    else:
        print(client_loan)


def notice(clientid):
    Check_loan()
    client_data = pd.read_csv("Client Database.csv",
                              sep=",", header=0)

    client_loan = client_loans(client_data, clientid, "open")
    # print(len(client_loan))
    client_loan_data = client_loan

    today = datetime.date.today()
    loan_ids = 0
    total_due = 0
    # a = input()
    for i in client_loan_data.index:
        due_Date = client_loan_data.loc[i, "Due_date"]

        # print("due date", due_Date)
        if due_Date == "0":
            continue
        due_Date = datetime.date.fromisoformat(due_Date)
        if today > due_Date:
            loan_ids = client_loan_data.loc[i, "Loan_id"]
            total_due = client_loan_data.loc[i, "Due_amount"]
            print(
                "*******************************************************************************")
            print(
                f"NOTE !!!! DUE DATE MISSED FOR LOAN {loan_ids}  ! DUE AMOUNT IS {total_due} !!!    ")
            print(
                "*******************************************************************************")
        elif today == due_Date:
            loan_ids = client_loan_data.loc[i, "Loan_id"]
            total_due = client_loan_data.loc[i, "Due_amount"]
            print(
                "*******************************************************************************")
            print(
                f"NOTE !!!!! DUE DATE FOR LOAN {loan_ids} IS TODAY ! DUE AMOUNT IS {total_due} !!!  ")
            print(
                "*******************************************************************************")
        elif today >= due_Date - relativedelta(days=10):
            loan_ids = client_loan_data.loc[i, "Loan_id"]
            print(
                "*******************************************************************************")
            print(
                f"NOTE !!!!!!!! DUE DATE FOR LOAN {loan_ids} IS NEAR ! DUE DATE IS {due_Date} !!!")
            print(
                "*******************************************************************************")
        else:
            pass


def check_due():
    client_data = pd.read_csv("Client Database.csv", sep=",", header=0)
    for index in client_data.index:
        if client_data.loc[index, "Status"] == "open":
            client_id = client_data.loc[index, "Client ID"]
            emi = client_data.loc[index, "EMI"]
            due_date = client_data.loc[index, "Due_date"]
            due_amount_ini = client_data.loc[index, "Due_amount"]
            due_amount = due_amount_cal(due_date, emi, due_amount_ini)
            client_data.loc[index, "Due_amount"] = due_amount

    client_data.to_csv("Client Database.csv", index=False)


def due_Date_cal(due_date_ini, Starting_date):
    Starting_date = datetime.date.fromisoformat(str(Starting_date))

    due_date_ini = datetime.date.fromisoformat(str(due_date_ini))

    if datetime.date.today() > due_date_ini:
        diff = relativedelta(datetime.date.today(), due_date_ini)
        due_months = diff.years * 12 + diff.months + 1
        if datetime.date.today().day == due_date_ini.day:
            due_months = due_months - 1

        """due_months = (datetime.date.today().year - due_date_ini.year) * \
            12 + (datetime.date.today().month - due_date_ini.month) + 1
        """
    else:
        due_months = 0

    # due_date = due_date_ini + relativedelta(months=due_months)

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
        # print("LOAN IS WAITING")
        print()
        due_amount = 0

    # due_months = due_Date_cal()
    else:
        due_date = datetime.date.fromisoformat(str(due_date))
        if datetime.date.today() > due_date:
            diff = relativedelta(datetime.date.today(), due_date)
            due_months = diff.years * 12 + diff.months
            # +1 as before it return months difference between due date and today but a month before due date also need to included
            # due amount are punishment so it not just adding emi also the amount before a month
            if datetime.date.today().day == due_date.day:
                due_amount = emi * (due_months)
            else:
                due_amount = emi * (due_months + 1)
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
            client_data.loc[i, "Balance_out"] = 0

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
    if inp.lower() == "q":
        while True:

            confirm = input(
                "Are you sure you want to go to MAIN MENU (YES/NO) : ")
            if confirm.lower() == "yes" or confirm.lower() == "y":
                raise ChildProcessError

            elif confirm.lower() == "no" or confirm.lower() == "n":
                break

            else:
                print()
                print("\nTRY AGAIN !")
                print()
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
        columns=["Loan_id", "Type of Loan", "Rate", "Loan_Amount", "Time", "Bal_Out", "EMI", "Due_date", "Due_amount", "Last Transaction Date", "NO_ofPayment", "Start_Date", "Status"])
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
            time = client_data.loc[index1, "Time"]
            balance_out = client_data.loc[index1, "Balance_out"]
            emi = client_data.loc[index1, "EMI"]
            """principal = client_data.loc[index1, "Monthly_Principal"]
            interest = client_data.loc[index1, "Monthly_Interest"]"""
            no_oftrans = client_data.loc[index1, "No_ofTransaction"]
            starting_date = client_data.loc[index1, "Starting_date"]
            due_date_ini = client_data.loc[index1, "Due_date"]
            due_amount_ini = client_data.loc[index1, "Due_amount"]
            status_client = client_data.loc[index1, "Status"]
            last_dateoftrans = client_data.loc[index1, "Last Transaction Date"]
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
                                       loan_amount, time, balance_out, emi, due_date, due_amount, last_dateoftrans, no_oftrans, starting_date, status_client]

            i = i + 1

    return client_loan_data
    # print(len(client_loan_data))
    """if len(client_loan_data) == 0:
        print("NO LOAN AMOUNT OUT STANDING")
    """

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
    last_index = 1
    for index in trans_data.index:
        if client_id == trans_data.loc[index, "Client ID"]:
            trans_hist.loc[last_index] = trans_data.loc[index, :]
            trans_amount = trans_amount + \
                trans_hist.loc[last_index, "Transaction_Amount"]
            last_index = last_index + 1
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


# down fuction are used in new loan


def get_loan_amount():
    while True:    # amount they can get from there cerdit score
        try:
            loan_amount = input("Enter The AMOUNT You Want : ")
            move_tomainmenu(loan_amount, "client")
            loan_amount = int(loan_amount)
            if loan_amount < 10000:
                print("AMOUNT MUST BE GREATER THEN 10 Thousand ")
                print()
                continue
            elif loan_amount > 50000000:
                print("AMOUNT MUST BE Less then 5 Cr. ")
                print()
                continue
        except ValueError:
            print("Try Again")
            print()
            continue
            # get_pricipal()
        break
    return loan_amount


def typeofloans():
    while True:
        print("\t+------+---------------------+----------+""\n\t|Sr No | Types of Loan       | Int Rate |\n\t""+------+---------------------+----------+""\n\t|  1.  | Education Loan      |    3 %   |\n\t|  2.  | Personal Loan       |    8 %   |\n\t|  3.  | Home Loan           |    6 %   |\n\t|  4.  | Vehicle Loan        |   4.5 %  |\n\t|  5.  | Business loan       |    9 %   |\n\t|  6.  | Aggriculture Loan   |   2.5 %  |\n\t""+------+---------------------+----------+")
        typeofloan = input("Enter Which Type of Loan You want : ")
        move_tomainmenu(typeofloan, "client")
        if (typeofloan == "1") or ("education" in typeofloan.lower()):
            print()
            tl = "| Education Loan    |"
            typeofloan = "Education Loan"
            ir = "3 %      |"
            int_rate = 3

        elif (typeofloan == "2") or ("personal" in typeofloan.lower()):
            print()
            tl = "| Personal Loan     |"
            typeofloan = "Personal Loan"
            ir = "8 %      |"
            int_rate = 8

        elif (typeofloan == "3") or ("home" in typeofloan.lower()):
            print()
            tl = "| Home Loan         |"
            typeofloan = "Home Loan"
            ir = "6 %      |"
            int_rate = 6

        elif (typeofloan == "4") or ("vehicle" in typeofloan.lower()):
            print()
            tl = "| Vehicle Loan      |"
            typeofloan = "Vehicle Loan"
            ir = "4.5 %    |"
            int_rate = 4.5

        elif (typeofloan == "5") or ("business" in typeofloan.lower()):
            print()
            tl = "| Business Loan     |"
            typeofloan = "Buisness Loan"
            ir = "9 %      |"
            int_rate = 9

        elif (typeofloan == "6") or ("aggriculture" in typeofloan.lower()):
            print()
            tl = "| Aggriculture Loan |"
            typeofloan = "Aggriculture Loan"
            ir = "2.5 %    |"
            int_rate = 2.5

        else:
            print("Try Again")
            # typeofloans()
            continue

        break
    print("\t +-------------------+----------+""\n\t | Type of Loan      | Int Rate |\n\t"" +-------------------+----------+""\n\t",
          tl, ir, "\n\t"" +-------------------+----------+")
    return [typeofloan, int_rate]


""" rate of intrest :-   for good cerdit score
                            1) education : - 3%
                            2) personal : - 8 %
                            3) home loan : - 6 %
                            4) vechical loan :- 4.5 %
                            5) bussiness loan :- 9 %
                            6) aggriculture loan:- 2.5 %
"""


def get_time():
    # its limit will be decide by creadit scroce
    while True:
        try:
            fortime = input("Enter For How Much Time(\"in Year\") : ")
            print()
            move_tomainmenu(fortime, "client")
            fortime = int(fortime)
            if fortime > 10 or fortime < 0:
                print("Please Enter 10 Years OR less years")
                print()
                continue

        except ValueError:
            print("Try Again")
            print()
            # get-time()
            continue

        break
    return fortime

# EMI


def agaist_mortage(loan_amount):
    while True:
        try:
            mortage = input(
                "Against Mortgage of (\"It must Be 25 % more than Amount of loan you want \") : ")
            print()
            move_tomainmenu(mortage, "client")
            mortage = int(mortage)

            more_than = loan_amount * 25/100 + loan_amount

            if mortage <= more_than:
                print("Please Enter 25 % more Amount Than LOAN AMOUNT!!  ")
                print()
                continue

            else:
                print("Its Perfect ! ")
                print()

        except ValueError:
            print()
            print("Try Again")
            print()
            continue
        break
    return mortage


def curr_format(value):
    value_str = '{:,.2f}'.format(value)
    fin_formatted_value = u"\u20B9" + f"{value_str}"
    return fin_formatted_value


def add_toCSV(clientid, loan_amount, time, typeofloan, int_rate, monthly_pay, mortage):
    client_data = pd.read_csv("Client Database.csv",
                              sep=",", header=0)

    sansacition_amount = 0
    bal_out = 0
    status_ofloan = "waiting"
    principal = interest = 0
    no_oftrans = 0
    # print(client_data)
    # print("last_index")
    last_index = len(client_data.index)
    # due_date = due_Date_cal(no_oftrans, str(start))
    due_date = 0
    end = 0
    start = 0
    due_amount = 0
    Last_Transaction_Date = 0
    # approve_Date = 0
    applied_date = datetime.date.today()
    # print(last_index)
    if last_index == 0:
        loan_id = 1001
    else:
        loan_id = client_data.loc[last_index - 1, "loan_id"] + 1

    new_loandata = [clientid, loan_id, typeofloan, status_ofloan,  int_rate, loan_amount, time,
                    bal_out, monthly_pay, Last_Transaction_Date, no_oftrans, start, end, due_date, due_amount, mortage, applied_date]

    # print(new_loandata)
    client_data.loc[last_index] = new_loandata

    client_data.to_csv(path_or_buf="Client Database.csv",
                       sep=",", index=False, mode="w")
    print("LOAN IS APPLIED FOR APPROVAL ! ONCE VERIFIED YOU WILL BE NOTIFY")
    print()


def new_loan(clientid):

    while True:
        print()
        print("WELCOME TO LOAN CALCULATER !!!!!!")
        print()

        loan_amount = get_loan_amount()
        type_rate = typeofloans()
        month = 12
        # print(type_rate)
        # print(type(type_rate[1]))
        # a = type_rate[1]
        typeofloan = type_rate[0]
        int_rate = type_rate[1]
        time = get_time()
        aga_mortage = agaist_mortage(loan_amount)
        cal_month_payment = monthly_pay_int(loan_amount, time, int_rate)
        month_payment = cal_month_payment
        total_pay = month_payment * time * month
        Interest_amount = total_pay - loan_amount
        rou_moth_pay = round(month_payment)
        rou_interest_amount = round(Interest_amount)
        rou_total_pay = round(total_pay)

        ending_date = datetime.date.today() + relativedelta(years=time)
        print("*******************************************************")
        print("Total Interest Amount will be : ",
              curr_format(rou_interest_amount))
        print("Loan will End at : ", ending_date)
        print("EMI will be : ", curr_format(rou_moth_pay))
        print("Total Payment will be : ", curr_format(rou_total_pay))
        print("*******************************************************")
        print()

        while True:
            print("*************************""\n* 1)GET LOAN with same  *\n* 2)Calculate agian     *\n* 3)Return To Main Menu *""\n*************************")
            choice = input("ENTER HERE : ")
            move_tomainmenu(choice, "client")
            if choice == "1" or "get loan" in choice.lower():
                con_no = 0
                while con_no <= 3:
                    confirm = input("\nWant To Continue (YES or NO):")
                    move_tomainmenu(confirm, "client")
                    if confirm.lower() == "yes" or confirm.lower() == "y":
                        add_toCSV(clientid, round(loan_amount), time,
                                  typeofloan, int_rate, rou_moth_pay, aga_mortage)
                        print("Thank You !")
                        print()
                        # main mane
                    elif confirm.lower() == "no" or confirm.lower() == "n":
                        print()
                        # exec(open("Main_Menu.py").read())
                        break

                    else:
                        print("TRY AGAIN ! ANSWER ", 3 - con_no, "try left")
                        print()
                        con_no = con_no + 1
                        continue
                    break
                break
            elif choice == "2" or "calculate agian" in choice.lower():
                print("LETS TRY AGAIN")
                print()
                break
            elif choice == "3" or "return to main menu" in choice.lower():
                print()
                break
            else:
                print("TRY AGAIN !")
                print()
                continue

        if choice == "2" or "calculate agian" in choice.lower():
            continue
        else:
            break

    # pay_now used


def make_transaction(client_id, typeofloan, emi, loan_id, due_amount):

    trans_data = pd.read_csv("Transaction_Database.csv")
    last_index = len(trans_data.index)

    while True:
        Trans_no_check = random.randrange(11111111, 99999999, 1)
        for p in trans_data["Transaction ID"]:

            if (p == Trans_no_check):
                continue
        Trans_id = Trans_no_check
        break

    date_today = datetime.date.today()
    Transaction_Mode = "ONLINE BANKING"
    total_pay = emi+due_amount
    # Client ID,Transaction ID,Type of Loans,Date of Transaction,Transaction_Amount,Transaction_Mode
    trans_data.loc[last_index] = [client_id, loan_id, Trans_id,
                                  typeofloan, date_today, emi, due_amount, total_pay, Transaction_Mode]

    trans_data.to_csv("Transaction_Database.csv", index=False)
    print()


def pay_now(clientid):
    Check_loan()
    client_data = pd.read_csv("Client Database.csv",
                              sep=",", header=0)
    # print(client_data["Client ID"])
    client_loan_data = client_loans(client_data, clientid, "open")
    # print(len(client_loan))
    # client_loan_data = client_loan
    if len(client_loan_data) == 0:
        print()
        print("NO LOAN AMOUNT OUT STANDING")
        print()
        raise ChildProcessError

    print(client_loan_data)

    while True:
        try:
            cho_pay_for_check = input(
                "Enter For which Loan you want to pay (Enter Index) or Q to quit: ")
            print()
            move_tomainmenu(cho_pay_for_check, "client")
            cho_pay_for_check = int(cho_pay_for_check)
            if cho_pay_for_check in client_loan_data.index.tolist():
                cho_pay_for = cho_pay_for_check
                break
            else:
                print()
                print("ENTER VALID !")
                print()
                continue

        except ValueError:
            print()
            print("TRY AGAIN !")
            print()
            continue
            # exec(open("Main_Menu.py").read())
            # break
            # a = input()

    client_loan_data_chose = client_loan_data.loc[cho_pay_for]
    client_loan_data_chose.Name = "YOU WILL PAY FOR"
    print()
    print("YOU HAVE SELECTED !!! ")
    print()
    print(client_loan_data_chose)
    print()

    loan_id = client_loan_data_chose["Loan_id"]
    typeofloan = client_loan_data_chose["Type of Loan"]
    ini_balance_out = client_loan_data_chose["Bal_Out"]
    loan_amount = client_loan_data_chose["Loan_Amount"]
    emi = client_loan_data_chose["EMI"]
    """principal = client_loan_data_chose["Monthly Principal"]
    interest = client_loan_data_chose["Monthly Interest"]"""
    no_oftrans = client_loan_data_chose["NO_ofPayment"]
    rate = client_loan_data_chose["Rate"]
    due_date = client_loan_data_chose["Due_date"]
    due_amount = client_loan_data_chose["Due_amount"]
    starting = client_loan_data_chose["Start_Date"]
    time = client_loan_data_chose["Time"]

    # emi_paid = due_amount/emi
    Starting_date = datetime.date.fromisoformat(str(starting))
    # as he will pay for this month
    ending_date = Starting_date + relativedelta(years=time)
    due_date = datetime.date.fromisoformat(str(due_date))
    due_payments = due_amount/emi
    if datetime.date.today() > ending_date:
        topay_emi = 0
    else:
        topay_emi = emi
    total_pay = topay_emi + due_amount
    print(
        f"YOU WILL PAY FOR EMI {curr_format(topay_emi)} AND DUE AMOUNT {curr_format(due_amount)} : ", curr_format(total_pay))
    print()
    # confirm = input("ARE YOU SURE TO PAY (YES or NO):")
    # print(emi)
    con_no = 0
    while con_no <= 3:
        confirm = input("\nWant To Continue (YES or NO):")
        move_tomainmenu(confirm, "client")
        if confirm.lower() == "yes" or confirm.lower() == "y":
            make_transaction(clientid, typeofloan,
                             topay_emi, loan_id, due_amount)
            """thismonth_interest = ini_balance_out * rate/100/12
            thismonth_principal = emi - thismonth_interest
            Total_principal = principal + thismonth_principal
            Total_interest = thismonth_interest + interest"""
            no_oftrans = no_oftrans + 1
            due_amount = 0

            due_months = due_Date_cal(due_date, Starting_date)
            # print("due months", due_months)
            due_date_fin = due_date + relativedelta(months=due_months + 1)
            # print(due_date_fin, due_date_fin.month)
            diff = relativedelta(due_date_fin, Starting_date)
            bal_month = diff.years * 12 + diff.months - 1
            """bal_month = due_date_fin.year - Starting_date.year) * \
                12 + (due_date_fin.month - Starting_date.month) - 1"""
            # print(bal_month)
            fin_balance_out = bal_calculater(
                loan_amount, rate, time, bal_month)

            if due_date_fin >= ending_date:
                due_date_fin = ending_date

            fin_month_interest = fin_balance_out * rate / 100 / 12
            fin_month_principal = emi - fin_month_interest

            # print(emi)
            # due_date = due_Date_cal( loan_amount, balance_out, emi, starting)
            for i in client_data.index:
                if loan_id == client_data.loc[i, "loan_id"]:
                    # print("here")
                    client_data.loc[i, "Balance_out"] = round(
                        fin_balance_out)
                    """client_data.loc[i, "Monthly_Principal"] = round(
                        fin_month_principal)
                    client_data.loc[i, "Monthly_Interest"] = round(
                        fin_month_interest)"""
                    client_data.loc[i, "No_ofTransaction"] = no_oftrans
                    client_data.loc[i, "Due_date"] = due_date_fin
                    client_data.loc[i, "Due_amount"] = due_amount
                    client_data.loc[i, "Last Transaction Date"] = str(
                        datetime.date.today())
                    """print("\nBalance Out : ", fin_balance_out, "\nMonthly Principal Amount :",
                        thismonth_principal, "\nMonthy Int Rate :", thismonth_interest)"""
            client_data.to_csv("Client Database.csv", index=False)
            # print(client_data)
            print("Thank You!")
            print()
            # main mane
        elif confirm.lower() == "no" or confirm.lower() == "n":
            print()
            # exec(open("Main_Menu.py").read())
            # quit()
            break
        else:
            print("TRY AGAIN ANSWER ", 3 - con_no, "try left")
            print()
            con_no = con_no + 1
            continue
        break
    Check_loan()

# payment sch


def show_graph(loan_transaction):

    principal = loan_transaction["Monthly Principal"]
    bal_out = loan_transaction["Bal_out"]
    emi = loan_transaction["EMI"]
    mon_int = loan_transaction["Monthly Interest"]
    # print("time", loan_transaction["DUE DATE"])
    time = loan_transaction["DUE DATE"]

    plt.figure(figsize=(7, 5))
    loan_amount = bal_out.head(1).values[0]
    plt.plot(time, principal, color="r")
    plt.plot(time, emi, color="g")
    plt.plot(time, mon_int, color="b")
    plt.grid(True)
    emi = emi.loc[1]
    # print(emi)
    emi_round = round(emi,  - (len(str(emi)) - 1))
    # print(emi_round)
    emi_Start = str(emi_round)[0]
    # print(emi_round / int(emi_Start))
    emi_round_1 = emi_round + emi_round / int(emi_Start)
    # print(emi_round_1)
    plt.yticks(
        list(range(0, int(emi_round_1) + 1, int(emi_round / 10))))

    # int(emi_round) + int(emi_round / 2)
    plt.yscale("linear")

    plt.xlabel("DUE DATES")
    plt.ylabel("RUPEES")
    plt.title("PAYMENT SCHEDULE GRAPH")
    plt.legend(["PRINCIPAL", "BAL_OUT", "MON_INT"])

    plt.show()


def pay_shcd(clientid):

    client_data = pd.read_csv("Client Database.csv",
                              sep=",", header=0)

    client_loan = client_loans(client_data, clientid, "open")
    client_loan_data = client_loan

    if len(client_loan_data) == 0:
        print("NO LOAN AMOUNT OUT STANDING")
        print()

    else:

        print(client_loan_data)
        while True:
            try:
                cho_pay_for = input(
                    "Enter For which Loan you want to Check (Enter Index): ")
                print()
                move_tomainmenu(cho_pay_for, "client")
                cho_pay_for = int(cho_pay_for)
                if cho_pay_for not in client_loan_data.index.tolist():
                    print("TRY AGIAN")
                    continue
                break
            except ValueError:
                continue

        i = 1

        """    for cho_pay_for in client_loan_data.index:
            # print("open" == client_data.loc[cho_pay_for, "Status"])
            # print(client_data.loc[cho_pay_for, "Status"])
            # "open" == client_data.loc[cho_pay_for, "Status"].lower():
            if cho_pay_for == cho_pay_for:
        """

        ch_loan_amount = client_loan_data.loc[cho_pay_for, "Loan_Amount"]
        ch_rate = client_loan_data.loc[cho_pay_for, "Rate"]
        ch_time = client_loan_data.loc[cho_pay_for, "Time"]
        ch_emi = client_loan_data.loc[cho_pay_for, "EMI"]
        ch_due_date = client_loan_data.loc[cho_pay_for, "Due_date"]
        starting_Date = client_loan_data.loc[cho_pay_for, "Start_Date"]
        # ch_trans = client_loan_data.loc[cho_pay_for, "NO_ofPayment"]
        ini_month_int = ch_loan_amount * ch_rate / 100 / 12
        ini_principal = ch_emi - ini_month_int
        loan_transaction = pd.DataFrame(
            columns=["Bal_out", "Monthly Principal", "Monthly Interest", "EMI", "DUE DATE"])
        Starting_date = datetime.date.fromisoformat(
            str(starting_Date))
        # as he will pay for this month
        # print("now")
        # loan_transaction.loc[0, :] = [
        #   ch_loan_amount, ini_principal, ini_month_int, ch_emi, ch_due_date]
        ch_trans = 1
        while True:
            if ch_trans == 1:
                bal_out = ch_loan_amount
                due_date = Starting_date + relativedelta(months=1)
                loan_transaction.loc[ch_trans, :] = [
                    round(bal_out), round(ini_principal), round(ini_month_int), ch_emi, due_date]
                ch_trans = ch_trans + 1
                continue
            else:

                for month in range(1, ch_time * 12):

                    # bal_out = loan_transaction.loc[ch_trans-1, "Bal_out"]
                    bal_out = bal_calculater(
                        ch_loan_amount, ch_rate, ch_time, month)
                    month_int = bal_out * ch_rate / 100 / 12
                    principal = ch_emi - month_int
                    # bal_out = bal_out - principal
                    # due_Date = due_Date_cal(ch_trans, starting_Date)

                    due_date = Starting_date + \
                        relativedelta(months=ch_trans)

                    loan_transaction.loc[ch_trans, :] = [
                        round(bal_out), round(principal), round(month_int), round(ch_emi), due_date]
                    ch_trans = ch_trans + 1
                break
                # if len(loan_transaction.index) == 0:
            #       last_index = 1
            #  else:
            #     last_index = len(client_loan_data.index) + 1

            #  print(last_index)

        print(loan_transaction)
        print()
        print("TOTAL PRINCIPAL : ", curr_format(sum(
            loan_transaction["Monthly Principal"])))
        print()
        print("TOTAL INTEREST : ", curr_format(sum(
            loan_transaction["Monthly Interest"])))
        print()
        print("TOTAL PAYMENT WILL BE :", curr_format(
            sum(loan_transaction["EMI"])))

        show_graph(loan_transaction)

# emp use


def verify_loan():

    client_data = pd.read_csv("Client Database.csv",
                              sep=",", header=0)

    waiting_Database = pd.DataFrame(columns=client_data.columns)
    row = 1
    for i in client_data.index:
        if client_data.loc[i, "Status"].lower() == "waiting":
            waiting_Database.loc[row] = client_data.loc[i, :]
            row = row + 1
    if len(waiting_Database) == 0:
        print()
        print("NO Waiting LOANS !")
        print()

    else:

        while True:
            print()
            print(waiting_Database)
            try:
                print()
                cho_toapp = input(
                    "ENTER INDEX YOU WANT TO APPROVE OR DENY FOR : ")
                print()
                move_tomainmenu(cho_toapp, "emp")
                cho_toapp = int(cho_toapp)

                if cho_toapp in waiting_Database.index.tolist():
                    print(waiting_Database.loc[cho_toapp])
                    print()
                    print(
                        "\t\t*************""\n\t\t* 1)APPROVE *\n\t\t* 2)DENY    *\n\t\t""*************")
                    ans = input("ENTER YOUR CHOICE : ")
                    print()
                    move_tomainmenu(ans, "emp")

                    loan_id_verifi = waiting_Database.loc[cho_toapp, "loan_id"]

                    if ans == "1" or ans.lower() == "approve":
                        print("VERIFIED")
                        # print(ans, "1")
                        for j in client_data.index:
                            if loan_id_verifi == client_data.loc[j, "loan_id"]:
                                # print("match")
                                # due_date_ini = client_data.loc[j, "Due_date"]
                                time = client_data.loc[j, "Time"]
                                Starting_date = datetime.date.today()
                                ending_date = Starting_date + \
                                    relativedelta(years=time)
                                due_date_ini = Starting_date + \
                                    relativedelta(months=1)
                                # due_date = due_Date_cal(due_date_ini)
                                client_data.loc[j,
                                                "Starting_date"] = Starting_date
                                client_data.loc[j, "Ending_date"] = ending_date
                                client_data.loc[j, "Due_date"] = due_date_ini
                                client_data.loc[j, "Status"] = "open"
                                client_data.loc[j,
                                                "Balance_out"] = client_data.loc[j, "Loan_amount"]
                                waiting_Database = waiting_Database.drop(
                                    index=cho_toapp)
                                break
                        break
                    elif ans == "2" or ans.lower() == "deny":
                        for k in client_data.index:
                            if loan_id_verifi == client_data.loc[k, "loan_id"]:
                                # print("HERE", loan_id_verifi)
                                client_data = client_data.drop(index=k)
                                waiting_Database = waiting_Database.drop(
                                    index=cho_toapp)
                                break
                        break

                    else:
                        print("ENTER VALID !!!")
                        print()
                        continue

                    # print("HERE")

                else:
                    print("ENTER VALID")
                    print()
                    continue

            except ValueError:
                print("TRY Again !")
                print()
                continue

        # print(client_data)
        client_data.to_csv("Client Database.csv", index=False)
        # print(waiting_Database)
