import pandas as pd
from getpass import getpass


def login():

    while True:
        try:

            databas = pd.read_csv("Employ_Database.csv", sep=",",
                                  header=0)
            # databas.index
            # print(databas)

            loginid = databas["Employ ID"]
            # print(loginid)
            i = 0
            while i < 5:

                input_id = int(input("ENTER YOUR EMP ID :"))

                for index in loginid.index:

                    #print(dataid, type(dataid))
                    #print(dataid == input_id)
                    if int(loginid[index]) == input_id:
                        idindex = index
                        # print(idindex)
                        print("ID is matched : ", input_id)
                        while True:
                            password = getpass("ENTER YOUR PASSWORD : ")
                            if str(password) == str(databas.loc[index, "Password"]):
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
        except KeyError:
            print("TRY AGAIN !! ")
            # while True:
            continue

    return input_id


empid = login()
