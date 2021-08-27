import pandas as pd
from login import clientid
from main import client_loans, due_Date_cal, move_tomainmenu
import math


def bal_calculater(loan_amount, rate, time, months, emi):

    rate_formated = rate / 100 / 12
   # months = time * 12
  #  print(months)
  #  print(emi)
    a = math.pow((1 + rate_formated), time * 12)
    b = a - 1
    bal_amount = loan_amount * (a - math.pow((1 + rate_formated), months)) / b
    # print(bal_amount)

    return bal_amount

# client_loan


client_data = pd.read_csv("Client Database.csv",
                          sep=",", header=0)


client_loan = client_loans(client_data, clientid, "open")
client_loan_data = client_loan


"""balance_out = client_loan[1]
emi = client_loan[2]
typeofloan = client_loan[3]
principal = client_loan[4]
rate = client_loan[5]
principal = client_loan[6]
interest = client_loan[7]
loan_id = client_loan[8]
no_oftrans = client_loan[9]
due_date = client_loan[10]"""
# due_amount = client_loan[11]


if len(client_loan_data) == 0:
    print("NO LOAN AMOUNT OUT STANDING")

else:

    print(client_loan_data)
    cho_pay_for = int(
        input("Enter For which Loan you want to Check (Enter Index): "))
    move_tomainmenu(cho_pay_for, "client")

    i = 1
    for index1 in client_loan_data.index:
        # print("open" == client_data.loc[index1, "Status"])
        # print(client_data.loc[index1, "Status"])
        # "open" == client_data.loc[index1, "Status"].lower():
        if cho_pay_for == index1:

            ch_loan_amount = client_loan_data.loc[index1, "Loan_Amount"]
            ch_rate = client_loan_data.loc[index1, "Rate"]
            ch_time = client_loan_data.loc[index1, "Time"]
            ch_emi = client_loan_data.loc[index1, "EMI"]
            ch_due_date = client_loan_data.loc[index1, "Due_date"]
            starting_Date = client_loan_data.loc[index1, "Start_Date"]
            #ch_trans = client_loan_data.loc[index1, "NO_ofPayment"]
            ini_month_int = ch_loan_amount * ch_rate / 100 / 12
            ini_principal = ch_emi - ini_month_int
            loan_transaction = pd.DataFrame(
                columns=["Bal_out", "Principal", "Monthly Interest", "EMI", "DUE DATE"])
            # print("now")
            loan_transaction.loc[0, :] = [
                ch_loan_amount, ini_principal, ini_month_int, ch_emi, ch_due_date]
            ch_trans = 2
            for month in range(1, ch_time * 12 + 1):

                bal_out = bal_calculater(
                    ch_loan_amount, ch_rate, ch_time, month, ch_emi)
                month_int = bal_out * ch_rate / 100 / 12
                principal = ch_emi - month_int

                due_Date = due_Date_cal(ch_trans, starting_Date)
                ch_trans = ch_trans + 1
            # if len(loan_transaction.index) == 0:
            #       last_index = 1
            #  else:
            #     last_index = len(client_loan_data.index) + 1

            #  print(last_index)

                loan_transaction.loc[month, :] = [
                    bal_out, principal, month_int, ch_emi, due_Date]

            print(loan_transaction)
        else:
            print("")
