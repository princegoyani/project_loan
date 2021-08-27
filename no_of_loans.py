import pandas as pd
from login import clientid
from dateutil.relativedelta import relativedelta
from main import client_loans, move_tomainmenu


def choose_loan():
    print("******************")
    print("* 1.ALL LOANS    *\n* 2.CURRENT LOAN *\n* 3.WAITING LOAN *\n* 4.EXPIRE LOAN  *")
    print("******************")
    while True:

        ch = input("ENTER YOUR CHOICE : ")
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
    return status_client


client_data = pd.read_csv("Client Database.csv",
                          sep=",", header=0)

status_client = choose_loan()
client_loan = client_loans(client_data, clientid, status_client)
if len(client_loan) == 0:
    print("NO LOAN AMOUNT OUT STANDING")
else:
    print(client_loan)

#
#
#
#
#
""""client_ids = client_data["Client ID"]
client_loan_data = pd.DataFrame(
    columns=["Loan", "Rate", "Principal", "Status", "San_Amount", "Time", "Bal_Out", "EMI", "Due_date", "Due_amount"])
# print(client_ids)
i = 1
for index1 in client_ids.index:
   # print("" == client_data.loc[index1, "Status"])
    #print(client_data.loc[index1, "Status"])
    if clientid == client_ids[index1] and client_data.loc[index1, "Status"].lower() in status_client:
        loan_id = client_data.loc[index1, "loan_id"]
        stat = client_data.loc[index1, "Status"]
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
        print(due_date_ini)
        print(starting_date)
        due_date = due_Date_cal(
            loan_amount, balance_out, emi, no_oftrans, starting_date)

        due_amount = due_amount_cal(
            due_date, emi, balance_out, due_amount_ini)
        client_loan_data.loc[i] = [typeofloan, rate,
                                   principal, stat, san_amount, time, balance_out, emi, due_date, due_amount]

        i = i + 1


print(client_loan_data)
"""
