from getpass import getpass
from numpy import who
import pandas as pd
import random


def login():

    while True:
        try:

            databas = pd.read_csv("ClientLoginInfo.csv", sep=",",
                                  header=0)
            # databas.index
            # print(databas)

            loginid = databas["Client ID"]
            # print(loginid)
            i = 0
            while i < 5:

                input_id = int(input("ENTER YOUR CUSTOUMER ID :"))

                for index in loginid.index:
                    dataid = loginid[index]
                    # print(dataid, type(dataid))
                    # print(dataid == input_id)
                    if dataid == input_id:
                        idindex = index
                        # print(idindex)
                        print("ID is matched : ", dataid)
                        while True:
                            password = getpass("ENTER YOUR PASSWORD : ")
                            if str(password) == str(databas.loc[idindex, "Password"]):
                                print("PASWORD MATCH")
                                # START FROM HERE
                                break
                            else:
                                print("Password Incorrect !!!!! ")
                                continue
                        break
                else:
                    print("INVALID ID !!!!! ")
                    print("TRY AGAIN - ")
                    i = i + 1
                    continue
                break

            else:
                print("TRY AGAIN LATER")
            break
        except ValueError:
            print("TRY AGAIN !! ")
            # while True:
            continue

    return dataid


def registration():

    database = pd.read_csv("Client_Personal_Info.csv", sep=",", header=0)

    l_index = database.tail(1).index[0]
    # last_client_id = database.loc[l_index, "Client ID"]
    while True:
        acc_no_check = random.randrange(11111111, 99999999, 1)
        for p in database["ACCOUNT No"]:
            if (p == acc_no_check):
                continue
        acc_no = acc_no_check
        break

    cust_name = input("Enter Your Full Name : ")

    while True:
        try:
            mobile_number_check = int(input("Enter Your Mobile Number : "))
            if len(str(mobile_number_check)) == 10:
                if mobile_number_check in database["Mobile Number"]:
                    print('ALREDY USED')
                    continue

                else:
                    print("DONE")
                    mobile_number = mobile_number_check
                    break

            else:
                print("ENTER VALID NUMBER ")
                continue
        except ValueError:
            print("ENTER VALID NUMBER ")
            continue

    add = input("Enter Your Address : ")

    login_database = pd.read_csv("ClientLoginInfo.csv")
    l_login_index = login_database.tail(1).index[0]

    client_id = login_database.loc[l_login_index, "Client ID"] + 1
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
            login_database.loc[l_login_index + 1] = [client_id, password]
            break
        else:
            print("TRY AGAIN !")
            continue

    print(f"Your CLIENT ID IS : {client_id}")

    database.to_csv('Client_Personal_Info.csv', index=False)
    login_database.to_csv("ClientLoginInfo.csv", index=False)


while True:

    client_chos = input("1)LOGIN \n2)Registration : \n")
    if client_chos == "1" or "login" == client_chos.lower():
        clientid = login()
        break
    elif client_chos == "2" or "registration" == client_chos.lower():
        registration()
        print("NOW YOU HAVE TO LOGIN !!! ")
        clientid = login()
        break
    else:
        print("TRY AGAIN !")
