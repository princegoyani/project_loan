import pandas as pd
from login import clientid
import datetime
import random
from dateutil.relativedelta import relativedelta
from main import due_Date_cal, due_amount_cal, client_loans, Check_loan, move_tomainmenu
import time


def transaction(client_id, typeofloan, emi, loan_id, due_amount):

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

print(client_loan_data)

# print(len(client_loan))

# client_loan_data = client_loan

if len(client_loan_data) == 0:
    print("NO LOAN AMOUNT OUT STANDING")
    import Main_Menu


while True:
    try:
        cho_pay_for_check = int(
            input("Enter For which Loan you want to pay (Enter Index) or Q to quit: "))
        move_tomainmenu(cho_pay_for_check, "client")
        if cho_pay_for_check in client_loan_data.index.tolist():
            cho_pay_for = cho_pay_for_check
            break
        else:
            print("ENTER VALID !")
            continue

    except:
        print("TRY LATER !")
        print("QUIT")
        quit()

        break

#a = input()

client_loan_data_chose = client_loan_data.loc[cho_pay_for]
print()
print("YOU HAVE SELECTED !!! ")
print()
print(client_loan_data_chose)
print()

loan_id = client_loan_data_chose["Loan_id"]
typeofloan = client_loan_data_chose["Loan"]
balance_out = client_loan_data_chose["Bal_Out"]
loan_amount = client_loan_data_chose["Loan_Amount"]
emi = client_loan_data_chose["EMI"]
principal = client_loan_data_chose["Total Principal"]
interest = client_loan_data_chose["Total Interest"]
no_oftrans = client_loan_data_chose["NO_ofPayment"]
rate = client_loan_data_chose["Rate"]
due_date = client_loan_data_chose["Due_date"]
due_amount = client_loan_data_chose["Due_amount"]
starting = client_loan_data_chose["Start_Date"]
print(
    f"YOU WILL PAY FOR EMI {emi} AND DUE AMOUNT {due_amount} : ", emi + due_amount)
print()
# confirm = input("ARE YOU SURE TO PAY (YES or NO):")

con_no = 0
while con_no <= 3:
    confirm = input("\nWant To Continue (YES or NO):")
    move_tomainmenu(confirm, "client")
    if confirm.lower() == "yes" or confirm.lower() == "y":
        transaction(clientid, typeofloan, emi, loan_id, due_amount)

        thismonth_interest = balance_out * rate/100/12
        thismonth_principal = emi - thismonth_interest
        Total_principal = principal + thismonth_principal
        Total_interest = thismonth_interest + interest
        balance_out = balance_out - thismonth_principal
        no_oftrans = no_oftrans + 1
        due_amount = 0
        due_date = due_Date_cal(no_oftrans, starting)
        for i in client_data.index:
            if loan_id == client_data.loc[i, "loan_id"]:
                client_data.loc[i, "Balance_out"] = balance_out
                client_data.loc[i, "Total_Principal"] = Total_principal
                client_data.loc[i, "Total_Interest"] = Total_interest
                client_data.loc[i, "No_ofTransaction"] = no_oftrans
                client_data.loc[i, "Due_date"] = due_date
                client_data.loc[i, "Due_amount"] = due_amount

        client_data.to_csv("Client Database.csv", index=False)
        print("Thank You!")
        # main mane
    elif confirm.lower() == "no" or confirm.lower() == "n":
        print("main manu")
        import Main_Menu
        # quit()

    else:
        print("INVALID ANSWER ", 3 - con_no, "try left")
        con_no = con_no + 1
        continue
    break


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
