import pandas as pd
from login import clientid
from main import client_loans, move_tomainmenu

import datetime
from dateutil.relativedelta import relativedelta
from main import bal_calculater
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def show_graph(loan_transaction):
    principal = loan_transaction["Principal"]
    bal_out = loan_transaction["Bal_out"]
    emi = loan_transaction["EMI"]
    mon_int = loan_transaction["Monthly Interest"]
    # print("time", loan_transaction["DUE DATE"])
    time = loan_transaction["DUE DATE"]

    # graph_Data = pd.DataFrame([bal_out, principal, mon_int], index=time)

    # plt.plot(graph_Data)

    # plt.xticks(time)

    # time = date(loan_transaction["DUE DATE"]).year
    # print(time)
    """print(principal)
        print("BAL_OUT", bal_out)
        a = round(bal_out[1])
        print(round(a))"""
    # b = list(range(1000000, 10000000, 100000))
    # print(b)
    #print(bal_out.tail(1).values[0], type(bal_out.tail(1).values[0]))
    plt.figure(figsize=(7, 5))
    loan_amount = bal_out.head(1).values[0]
    plt.plot(time, principal, color="r")
    plt.plot(time, emi, color="g")
    plt.plot(time, mon_int, color="yellow")
    plt.grid(True)
    emi = emi.loc[1]
    print(emi)
    emi_round = round(emi,  - (len(str(emi)) - 1))
    print(emi_round)
    emi_Start = str(emi_round)[0]
    print(emi_round / int(emi_Start))
    emi_round_1 = emi_round + emi_round / int(emi_Start)
    print(emi_round_1)
    plt.yticks(
        list(range(0, int(emi_round_1) + 1, int(emi_round / 10))))

    # int(emi_round) + int(emi_round / 2)
    plt.yscale("linear")
    #
    # plt.yticks(b)
    # bal_out[0], bal_out.tail(1), principal))
    # plt.yticks(list(range(1000000, 10000000, 2000000)))
    # plt.ticklabel_format(useOffset=False)
    plt.xlabel("Due DATES")
    plt.ylabel("RUPESS")
    plt.title("PAYMENT SCH GRAPH")
    plt.legend(["PRICIPAL", "BAL_OUT", "MON_INTE"])

    plt.show()


"""def bal_calculater(loan_amount, rate, time, months, emi):

    rate_formated = rate / 100 / 12
   # months = time * 12
  #  print(months)
  #  print(emi)
    a = math.pow((1 + rate_formated), time * 12)
    b = a - 1
    bal_amount = loan_amount * (a - math.pow((1 + rate_formated), months)) / b
    # print(bal_amount)

    return bal_amount
"""
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
    cho_pay_for = input(
        "Enter For which Loan you want to Check (Enter Index): ")
    move_tomainmenu(cho_pay_for, "client")
    cho_pay_for = int(cho_pay_for)
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
            # ch_trans = client_loan_data.loc[index1, "NO_ofPayment"]
            ini_month_int = ch_loan_amount * ch_rate / 100 / 12
            ini_principal = ch_emi - ini_month_int
            loan_transaction = pd.DataFrame(
                columns=["Bal_out", "Principal", "Monthly Interest", "EMI", "DUE DATE"])
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

                        #bal_out = loan_transaction.loc[ch_trans-1, "Bal_out"]
                        bal_out = bal_calculater(
                            ch_loan_amount, ch_rate, ch_time, month)
                        month_int = bal_out * ch_rate / 100 / 12
                        principal = ch_emi - month_int
                        #bal_out = bal_out - principal
                        #due_Date = due_Date_cal(ch_trans, starting_Date)

                        due_date = Starting_date + \
                            relativedelta(months=ch_trans)

                        loan_transaction.loc[ch_trans, :] = [
                            round(bal_out), round(principal), round(month_int), round(ch_emi), due_date]
                        ch_trans = ch_trans + 1
                        # if len(loan_transaction.index) == 0:
                #       last_index = 1
                #  else:
                #     last_index = len(client_loan_data.index) + 1

                #  print(last_index)

                    break

            print(loan_transaction)
        else:
            print("")

    show_graph(loan_transaction)
