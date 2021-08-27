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
                # if len(loan_transaction.index) == 0:
        #       last_index = 1
        #  else:
        #     last_index = len(client_loan_data.index) + 1

        #  print(last_index)
            break

    print(loan_transaction)
    print()
    print("TOTAL PRINCIPAL : ", sum(
        loan_transaction["Monthly Principal"]))
    print()
    print("TOTAL INTEREST : ", sum(
        loan_transaction["Monthly Interest"]))
    print()
    print("TOTAL PAYMENT WILL BE :", sum(loan_transaction["EMI"]))

    show_graph(loan_transaction)


"""STUFF"""
# graph_Data = pd.DataFrame([bal_out, principal, mon_int], index=time)

# plt.plot(graph_Data)

# plt.xticks(time)
#
# plt.yticks(b)
# bal_out[0], bal_out.tail(1), principal))
# plt.yticks(list(range(1000000, 10000000, 2000000)))
# plt.ticklabel_format(useOffset=False)
# time = date(loan_transaction["DUE DATE"]).year
# print(time)
"""print(principal)
        print("BAL_OUT", bal_out)
        a = round(bal_out[1])
        print(round(a))"""
# b = list(range(1000000, 10000000, 100000))
# print(b)
# print(bal_out.tail(1).values[0], type(bal_out.tail(1).values[0]))

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
