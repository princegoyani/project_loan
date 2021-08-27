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

                input_id = int(input("ENTER YOUR EMPLOY ID : "))

                for index in loginid.index:

                    #print(dataid, type(dataid))
                    #print(dataid == input_id)
                    if int(loginid[index]) == input_id:
                        idindex = index
                        # print(idindex)
                        print()
                        print("ID is matched : ", input_id)
                        print()
                        while True:
                            password = getpass("ENTER YOUR PASSWORD : ")
                            if str(password) == str(databas.loc[index, "Password"]):
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
        except KeyError:
            print()
            print("TRY AGAIN !! ")
            print()
            # while True:
            continue

    return input_id


empid = login()
