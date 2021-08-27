from numpy.lib.function_base import _quantile_is_valid
import pandas as pd
from datetime import date
from login import clientid
from main import monthly_pay_int, move_tomainmenu
#from pay_now import due_Date_cal
from dateutil.relativedelta import relativedelta


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
        typeofloan = input("+------+---------------------+----------+""\n|Sr No | Types of Loan       | Int Rate |\n""+------+---------------------+----------+""\n|  1.  | Education Loan      |    3 %   |\n|  2.  | Personal Loan       |    8 %   |\n|  3.  | Home Loan           |    6 %   |\n|  4.  | Vehicle Loan        |   4.5 %  |\n|  5.  | Bussiness loan      |    9 %   |\n|  6.  | Aggriculture Loan   |   2.5 %  |\n""+------+---------------------+----------+""\nEnter Which Type of Loan You want : ")
        move_tomainmenu(typeofloan, "client")
        if (typeofloan == "1") or ("education" in typeofloan.lower()):
            print()
            typeofloan = "Education Loan"
            int_rate = 3

        elif (typeofloan == "2") or ("personal" in typeofloan.lower()):
            print()
            typeofloan = "Personal loan"
            int_rate = 8

        elif (typeofloan == "3") or ("home" in typeofloan.lower()):
            print()
            typeofloan = "Home loan"
            int_rate = 6

        elif (typeofloan == "4") or ("vechical" in typeofloan.lower()):
            print()
            typeofloan = "Vechical loan"
            int_rate = 4.5
        elif (typeofloan == "5") or ("bussiness" in typeofloan.lower()):
            print()
            typeofloan = "Bussiness loan"
            int_rate = 9
        elif (typeofloan == "6") or ("aggriculture" in typeofloan.lower()):
            print()
            typeofloan = "Aggriculture loan"
            int_rate = 2.5
        else:
            print("TRY AGAIN ! input ")
            print("Try Again")
            # typeofloans()
            continue

        break
    print(typeofloan, int_rate)

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
                print("Please Enter 25 % more Amount !!  ")
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
    #print("VALUE :", value_str)
    return value_str


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
    #due_date = due_Date_cal(no_oftrans, str(start))
    due_date = 0
    end = 0
    start = 0
    due_amount = 0
    Last_Transaction_Date = 0
    #approve_Date = 0
    applied_date = date.today()
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


while True:
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

    ending_date = date.today() + relativedelta(years=time)
    print("Total Interest Amount will be : ", rou_interest_amount)
    print()
    print("Last date of loan completion will be nearly : ", ending_date)
    print()

    print("EMI will be : ", rou_moth_pay)
    print()
    print("Total Payment will be : ", rou_total_pay)
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
                    print("MAIN MENU")
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
            print("Main Menu")
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


#import main_man
