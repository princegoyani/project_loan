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
            acc_no = databas["ACCOUNT No"]
            # print(loginid)
            i = 0
            while i < 5:

                input_id = int(input("ENTER YOUR ACCOUNT NUMBER : "))

                for index in acc_no.index:
                    dataid = acc_no[index]
                    # print(dataid, type(dataid))
                    # print(dataid == input_id)
                    if dataid == input_id:
                        idindex = index
                        loginid_client = loginid.loc[index]
                        # print(idindex)

                        print()
                        print("ID is matched : ", dataid)
                        print()
                        while True:
                            password = getpass("ENTER YOUR PASSWORD : ")
                            if str(password) == str(databas.loc[idindex, "Password"]):
                                print()
                                print("PASSWORD MATCH")
                                print()
                                # START FROM HERE
                                break
                            else:
                                print()
                                print("Password Incorrect !!!!! ")
                                print()
                                continue
                        break
                else:
                    print()
                    print("INVALID ID !!!!! ")
                    print()
                    print("TRY AGAIN - ")
                    print()
                    i = i + 1
                    continue
                break

            else:
                print()
                print("TRY AGAIN LATER")
                print()
            break
        except ValueError:
            print()
            print("TRY AGAIN !! ")
            print()
            # while True:
            continue

    return loginid_client


def contain_digit(str):
    for i in str:
        if i.isdigit() == True:
            raise UnicodeError


def registration():
    database = pd.read_csv("Client_Personal_Info.csv", sep=",", header=0)
    if len(database) == 0:
        l_index = 0
        last_client_id = 100
    else:
        l_index = database.tail(1).index[0]
        last_client_id = database.loc[l_index, "Client ID"]

    while True:
        acc_no_check = random.randrange(11111111, 99999999, 1)
        for p in database["ACCOUNT No"]:
            if (p == acc_no_check):
                continue
        acc_no = acc_no_check
        break

    while True:
        try:
            first_name = input("Enter Your First Name : ").capitalize()
            last_name = input("Enter Your Last Name : ").capitalize()
            if len(first_name) <= 3 or len(last_name) <= 3:
                print()
                print("ENTER CORRECT NAME")
                print()
                continue
            contain_digit(first_name)
            contain_digit(last_name)
        except UnicodeError:
            print()
            print("TRY AGAIN")
            print()
            continue
        break

    cust_name = first_name + " " + last_name

    while True:
        try:
            mobile_number_check = int(input("Enter Your Mobile Number : "))
            if len(str(mobile_number_check)) == 10:

                if mobile_number_check in list(database.loc[:, "Mobile Number"]):
                    print('ALREADY USED')
                    print()
                    continue
                else:
                    print("DONE ")
                    print()
                    mobile_number = mobile_number_check
                    break

            else:
                print("ENTER VALID ! ")
                print()
                continue
        except:
            print("ENTER VALID NUMBER ")
            print()
            continue

    add = input("Enter Your Address : ")

    client_id = last_client_id + 1
    List = [client_id, acc_no, cust_name, mobile_number, add]
    database.loc[l_index + 1] = List

    login_database = pd.read_csv("ClientLoginInfo.csv")
    l_login_index = len(login_database) + 1

    while True:
        password = input("ENTER PASSWORD :")
        if len(password) < 8:
            print("RETRY WITH MORE THEN 8 CHARACTERS !")
            print()
            continue
        con_pass = input("CONFIRM PASSWORD :")
        if len(password) >= 8 and password == con_pass:
            # login page
            print("THANKS FOR REGISTRATION")
            print()
            login_database.loc[l_login_index] = [
                client_id, acc_no, password]
            break
        else:
            print("TRY AGAIN !")
            print()
            continue
    print("YOUR ACCOUNT NUMBER IS :", acc_no)
    print()
    print(f"Your CLIENT ID IS : {client_id}")
    print()

    database.to_csv('Client_Personal_Info.csv', index=False)
    login_database.to_csv('ClientLoginInfo.csv', index=False)


while True:

    print("******************")
    print("* 1)LOGIN        *\n* 2)Registration *")
    print("******************")
    print()
    client_chos = input("ENTER YOUR CHOICE : ")

    if client_chos == "1" or "login" == client_chos.lower():
        clientid = login()
        break
    elif client_chos == "2" or "registration" == client_chos.lower():
        registration()
        print()
        print("NOW YOU HAVE TO LOGIN !!! ")
        print()
        clientid = login()
        break
    else:
        print("TRY AGAIN !")
        print()
