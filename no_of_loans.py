import pandas as pd
from login import clientid
from dateutil.relativedelta import relativedelta
from main import client_loans, move_tomainmenu, Check_loan


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


Check_loan()
client_data = pd.read_csv("Client Database.csv", sep=",", header=0)

status_client = choose_loan()
client_loan = client_loans(client_data, clientid, status_client)
if len(client_loan) == 0:
    print("NO LOAN AMOUNT OUT STANDING")
    print()
else:
    print(client_loan)
