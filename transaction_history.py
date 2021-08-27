import pandas as pd
from login import clientid
from datetime import date
import random


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


trans = transaction(clientid)
trans_hist = trans[0]
trans_am = trans[1]


print(trans_hist)
print()
print("YOUR TOTAL NO. OF PAID AMOUNT IS : ", trans_am)
print()


"""    while True:
        # Trans_no_check = random.randrange(11111111, 99999999, 1)
        df = pd.DataFrame(columns=trans_data.columns)
        i = 0
        for check_index in trans_data.index:

            if (trans_data.loc[check_index, "Client ID"] == client_id):
                #print(trans_data.loc[check_index, :])
                df.loc[i] = trans_data.loc[check_index, :]
                #print("YOUR ID IS CORRECT : ",loginid)
                #print("YOUR INDEX ARE  :" , check_index)
                i = i + 1
            else:
                continue
             #   print("YOUR ID IS INCORRECT :",loginid)
            # break

            # continue
        break
    print(df)

"""
#loginid=int(input("ENTER YOUR ID :"))
'''trans_data = pd.read_csv("Transaction_Database.csv")
a = trans_data["Transaction_Amount"] '''

'''print("YOUR TOTAL NO. OF PAID AMOUNT IS : ",a)'''
# AA BAKI CHE
