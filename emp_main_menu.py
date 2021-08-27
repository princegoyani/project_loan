import employ_login
import pandas as pd
from main import client_loans, get_data_status, move_tomainmenu, check_due, curr_format, verify_loan
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

while True:
    try:
        check_due()
        client_data = pd.read_csv("Client Database.csv",
                                  sep=",", header=0)
        print()
        print("\t\t*-----------*-----------*---------*")
        print("\t\t|\t    | MAIN MENU |         |")
        print("\t\t|\t    *-----------*         |")
        print("\t\t|\t                          |")
        print("\t\t| 1)VERIFY LOANS                  |\n\t\t| 2)CHECK CUSTOMER'S WAITING LOAN |\n\t\t| 3)CHECK CUSTOMER'S CURRENT LOAN |\n\t\t| 4)CHECK CUSTOMER'S EXPIRED LOAN |\n\t\t| 5)CUSTOMER'S TOTAL LOAN AMOUNT  |\n\t\t| 6)TOTAL DUE AMOUNT              |\n\t\t| 7)RECENT TRANSACTION            |\n\t\t| 8)CHECK CLIENT PERSONAL DETAILS |\n\t\t| 9)LOG OUT                       |")
        print("\t\t|\t                          |")
        print("\t\t*---------------------------------*")
        print("PRESS 'q' TO RETURN TO MAIN MENU ANYWHERE IN THE PROGRAM!")
        print()
        print()
        ch = int(input("ENTER YOUR CHOICE : "))
        print()

        if ch == 1:
            print("1) VERFIY LOANS !!!")
            verify_loan()
            print()

        elif ch == 2:
            status = "waiting"
            client_datas_ofstatus = get_data_status(client_data, status)
            if len(client_datas_ofstatus) == 0:
                print(f"NO {status.upper()} LOAN OUTSTANDING")
                print()
            else:
                print("CUSTOMER'S WAITING LOAN ARE : ")
                print()
                print(client_datas_ofstatus)

        elif ch == 3:
            status = "open"
            client_datas_ofstatus = get_data_status(client_data, status)
            if len(client_datas_ofstatus) == 0:
                print(f"NO {status.upper()} LOAN OUTSTANDING")
                print()
            else:
                print("CUSTOMER'S CURRENT LOAN ARE : ")
                print()
                print(client_datas_ofstatus)

        elif ch == 4:
            status = "expired"
            client_datas_ofstatus = get_data_status(client_data, status)
            if len(client_datas_ofstatus) == 0:
                print(f"NO {status.upper()} LOAN OUTSTANDING")
                print()
            else:
                print("CUSTOMER'S EXPIRED LOAN ARE : ")
                print()
                print(client_datas_ofstatus)

        elif ch == 5:

            status = "open"
            client_datas_ofstatus = get_data_status(client_data, status)
            if len(client_datas_ofstatus) == 0:
                print(f"NO {status.upper()} LOAN OUTSTANDING")
                print()
            else:
                print("CUSTOMER'S TOTAL LOAN AMOUNT IS -> ")
                print()
                print(client_datas_ofstatus)
                print()
                print("TOTAL LOAN AMOUNT GRANTED IS : ", curr_format(sum(
                    client_datas_ofstatus.loc[:, "Loan_amount"])))
                print()

        elif ch == 6:
            print("TOTAL DUE AMOUNT")
            print()
            clients_datas = pd.DataFrame(
                columns=["client_ids", "loan_id", "Due_amount"])
            i = 1
            total_due = 0
            client_ids_pre = []
            for index in client_data.index:
                client_id = client_data.loc[index, "Client ID"]
        #        print(type(client_id))
    #         print(client_ids_pre)
    #          print(type(client_ids_pre))
                if client_id in client_ids_pre:
                    pass
                else:
                    #               print(type(client_ids_pre))
                    client_ids_pre.append(int(client_id))

                    client_data_temp = client_loans(
                        client_data, client_id, "open")
                    # print(client_data_temp)
                    sum_due = sum(client_data_temp.loc[:, "Due_amount"])
                    print("FOR CLIENT", client_id,
                          " DUE AMOUNT IS ", curr_format(sum_due))
                    print()
                    total_due = total_due + sum_due
    #            print(client_ids_pre)

            print("\nTOTAL DUE : ", curr_format(total_due))

        elif ch == 7:
            print("RECENT TRANSACTION : ")
            print()
            trans_data = pd.read_csv("Transaction_Database.csv")
            if len(trans_data) == 0:
                print("NO TRANSACTION")
            else:
                print(trans_data.sort_index(ascending=False))
        elif ch == 8:
            client_personal_Data = pd.read_csv(
                "Client_Personal_Info.csv")
            print(client_personal_Data)

        elif ch == 9:
            print("LOGGING OUT")
            os.abort()
        else:
            print("PLEASE RE ENTER YOUR CHOICE !!!")
            print()
            continue

    except ChildProcessError:  # used in q for returning to main menu
        print()
        continue
    except ModuleNotFoundError:
        print("INSTALL NECESSARY MODUALS !!! ")
        print("REQUIRED MODUAL :- 1) PANDAS 2) MATHPOTLIB")
        print()
        break
    except:
        print("TRY AGAIN !!")
        print("IF ANY PROBLEM CONTACT ADMIN")
        print()
        continue

    #
    #
    """loan_id = client_data_temp.loc[index, "Loan_id"]
            no_oftrans = client_data_temp.loc[index, "NO_ofPayment"]
            starting_date = client_data_temp.loc[index, "Start_Date"]
            due_amount_ini = client_data_temp.loc[index, "Due_amount"]
            emi = client_data_temp.loc[index, "EMI"]
            due_date = due_Date_cal(no_oftrans, starting_date)
            due_amount = due_amount_cal(due_date, emi, due_amount_ini)
            client_data_temp.loc[index, "Due_amount"] = due_amount
            client_data_temp.loc[index, "Due_date"] = due_date"""

    """if client_id in clients_datas.loc[:, "client_ids"].tolist():
                for k in clients_datas.index:
                    if client_id == clients_datas.loc[k, "client_ids"]:
                        clients_datas.loc[k,
                                          "due_amount"] = clients_datas.loc[k, "due_amount"] + due_amount
                        clients_datas = clients_datas.loc[k, "loan_id"].append(
                            loan_id)

            else:

                clients_datas.loc[i] = [client_id, [loan_id], due_amount]
            print(clients_datas)
"""
