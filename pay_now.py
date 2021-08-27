import pandas as pd
from pandas.core.indexing import check_bool_indexer
from login import clientid
import datetime
import random
from dateutil.relativedelta import relativedelta
from main import due_Date_cal, due_amount_cal, client_loans, Check_loan, move_tomainmenu, bal_calculater
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


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


Check_loan()
client_data = pd.read_csv("Client Database.csv",
                          sep=",", header=0)

#print(client_data["Client ID"])

client_loan_data = client_loans(client_data, clientid, "open")


# print(len(client_loan))

# client_loan_data = client_loan

if len(client_loan_data) == 0:
    print("NO LOAN AMOUNT OUT STANDING")
    raise ChildProcessError

print(client_loan_data)

while True:
    try:
        cho_pay_for_check = input(
            "Enter For which Loan you want to pay (Enter Index) or Q to quit: ")
        move_tomainmenu(cho_pay_for_check, "client")
        cho_pay_for_check = int(cho_pay_for_check)
        if cho_pay_for_check in client_loan_data.index.tolist():
            cho_pay_for = cho_pay_for_check
            break
        else:
            print("ENTER VALID !")
            continue

    except ValueError:
        print("TRY AGAIN !")
        continue
        # exec(open("Main_Menu.py").read())
        # break

#a = input()

client_loan_data_chose = client_loan_data.loc[cho_pay_for]
print()
print("YOU HAVE SELECTED !!! ")
print()
print(client_loan_data_chose)
print()

loan_id = client_loan_data_chose["Loan_id"]
typeofloan = client_loan_data_chose["Loan"]
ini_balance_out = client_loan_data_chose["Bal_Out"]
loan_amount = client_loan_data_chose["Loan_Amount"]
emi = client_loan_data_chose["EMI"]
principal = client_loan_data_chose["Total Principal"]
interest = client_loan_data_chose["Total Interest"]
no_oftrans = client_loan_data_chose["NO_ofPayment"]
rate = client_loan_data_chose["Rate"]
due_date = client_loan_data_chose["Due_date"]
due_amount = client_loan_data_chose["Due_amount"]
starting = client_loan_data_chose["Start_Date"]
time = client_loan_data_chose["Time"]
total_pay = emi + due_amount


thismonth_interest = ini_balance_out * rate/100/12
thismonth_principal = emi - thismonth_interest

#emi_paid = due_amount/emi
Starting_date = datetime.date.fromisoformat(str(starting))
# as he will pay for this month
ending_date = Starting_date + relativedelta(years=time)
due_date = datetime.date.fromisoformat(str(due_date))


print(
    f"YOU WILL PAY FOR EMI {emi} AND DUE AMOUNT {due_amount} : ", total_pay)
print()
# confirm = input("ARE YOU SURE TO PAY (YES or NO):")
# print(emi)
con_no = 0
while con_no <= 3:
    confirm = input("\nWant To Continue (YES or NO):")
    move_tomainmenu(confirm, "client")
    if confirm.lower() == "yes" or confirm.lower() == "y":
        make_transaction(clientid, typeofloan, emi, loan_id, due_amount)
        Total_principal = principal + thismonth_principal
        Total_interest = thismonth_interest + interest
        no_oftrans = no_oftrans + 1
        due_amount = 0

        due_months = due_Date_cal(due_date, Starting_date)
        #print("due months", due_months)
        due_date_fin = due_date + relativedelta(months=due_months + 1)
        #print(due_date_fin, due_date_fin.month)
        if due_date_fin >= ending_date:
            bal_month = (due_date_fin.year - Starting_date.year) * \
                12 + (due_date_fin.month - Starting_date.month) - 1
            # print(bal_month)
            fin_balance_out = bal_calculater(
                loan_amount, rate, time, bal_month)
            due_date_fin = ending_date
        else:
            bal_month = (due_date_fin.year - Starting_date.year) * \
                12 + (due_date_fin.month - Starting_date.month) - 1
            # print(bal_month)
            fin_balance_out = bal_calculater(
                loan_amount, rate, time, bal_month)

        # print(emi)
        #due_date = due_Date_cal(loan_amount, balance_out, emi, starting)
        for i in client_data.index:
            if loan_id == client_data.loc[i, "loan_id"]:
                # print("here")
                client_data.loc[i, "Balance_out"] = round(fin_balance_out)
                client_data.loc[i, "Total_Principal"] = round(
                    Total_principal)
                client_data.loc[i, "Total_Interest"] = round(Total_interest)
                client_data.loc[i, "No_ofTransaction"] = no_oftrans
                client_data.loc[i, "Due_date"] = due_date_fin
                client_data.loc[i, "Due_amount"] = due_amount
                print("bal_out : ", fin_balance_out, "monthly prinipal :",
                      thismonth_principal, "monthy int :", thismonth_interest)
        client_data.to_csv("Client Database.csv", index=False)
        # print(client_data)
        print("Thank You!")
        # main mane
    elif confirm.lower() == "no" or confirm.lower() == "n":
        print("Main MENU")
        # exec(open("Main_Menu.py").read())
        # quit()
        break
    else:
        print("INVALID ANSWER ", 3 - con_no, "try left")
        con_no = con_no + 1
        continue
    break
Check_loan()

# stuff

# Pricipal_amount, Sanctioned Amount,for YEAR ,Balance_out,EMI

# due date

# due amount


# client_loan
"""
        while True:

            try:
                cho = int(input(
                    "\n1 ) Return to Main menu  \n2)Try Again \n3)Quit \n:"))
                if cho == 1:
                    print("main_menu()")
                    break

                elif cho == 2:
                    print()

                elif cho == 3:
                    quit()
            except:
                print("Enter Valid")
                continue
"""
