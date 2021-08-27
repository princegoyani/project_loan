import pandas as pd
import random

database = pd.read_csv("Client_Personal_Info.csv", sep=",", header=0)

l_index = database.tail(1).index[0]
last_client_id = database.loc[l_index, "Client ID"]
while True:
    acc_no_check = random.randrange(11111111, 99999999, 1)
    for p in database["ACCOUNT No"]:
        if (p == acc_no_check):
            continue
    acc_no = acc_no_check
    break


cust_name = input("Enter Your Full Name : ")

while True:
    mobile_number_check = int(input("Enter Your Mobile Number : "))
    try:
        if len(mobile_number_check) == 10:
            for q in database["Mobile Number"]:
                if q == mobile_number_check:
                    print('ALREDY USED')
                    continue
                else:
                    print("DONE ")
                    mobile_number = mobile_number_check
                break
            break

        else:
            print("ENTER VALID NUMBER ")
            continue
    except:
        print("ENTER VALID NUMBER ")
        continue

add = input("Enter Your Address : ")

login_database = pd.read_csv("ClientLoginInfo.csv")
l_login_index = login_database.tail(1).index[0] + 1

client_id = last_client_id + 1
List = [client_id, acc_no, cust_name, mobile_number, add]
database.loc[l_index + 1] = List

while True:
    password = input("ENTER PASSWORD :")
    if len(password) < 8:
        print("RETRY WITH MORE THEN 8 CHARACTERS !")
        continue
    con_pass = input("CONFIRM PASSWORD :")
    if len(password) >= 8 and password == con_pass:
        # login page
        print("THANKS FOR REGISTRATIOn")
        login_database.loc[l_login_index] = [client_id, password]
        break
    else:
        print("TRY AGAIN !")
        continue

print(f"Your CLIENT ID IS : {client_id}")

database.to_csv('Client_Personal_Info.csv', index=False)


# print(database)
