# print(" 1.ADD NEW LOAN \n\n 2.CHECK CUSTOMER'S CURRENT LOAN \n\n 3.CHECK CUSTOMER'S TOTAL INSTALLMENTS \n\n 4.CHECK CUSTOMER'S TRANSACTIONS \n\n 5.CHECK CUSTOMER'S RATE OF INTEREST \n\n 6.CHECK CUSTOMER'S TOTAL LOAN AMOUNT  \n\n 7.CHECK CUSTOMER'S PAID AMOUNT OF CURRENT LOAN   \n\n 8.CHECK CUSTOMER'S UNPAID AMOUNT \n\n 9.CHECK CUSTOMER'S NEXT PAYMENT DATE \n\n 10.CHECK CUSTOMER'S LAST DATE FOR PAYING INSTALLMENT OF THIS MONTH \n\n 11.CHECK CUSTOMER'S TIME ALLOTED FOR LOAN COMPLETION (IN YEARS) \n")
# print()
from main import client_loans, get_data_status, move_tomainmenu
import pandas as pd
import employ_login
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


while True:
    try:
        client_data = pd.read_csv("Client Database.csv",
                                  sep=",", header=0)
        print("PRESS Q TO RETURN TO MAIN MENU ANYWHERE IN THE PROGRAM !")
        print("MAIN MENU \n""***********************************""\n* 1)VERIFY LOANS                  *\n* 2)CHECK CUSTOMER'S WAITING LOAN *\n* 3)CHECK CUSTOMER'S CURRENT LOAN *\n* 4)CHECK CUSTOMER'S EXPIRED LOAN *\n* 5)CUSTOMER'S TOTAL LOAN AMOUNT  *\n* 6)TOTAL DUE AMOUNT              *\n* 7)RECENT TRANSACTION            *\n* 8)CHECK CLIENT PERSONAL DETAILS *\n* 9)LOG OUT                       *\n""***********************************")
        ch = input("ENTER YOUR CHOICE : ")
        move_tomainmenu(ch, "emp")
        ch = int(ch)

        if ch == 1:
            print("1) VERFIY LOANS !!!")
            exec(open("emp_check.py").read())

        elif ch == 2:
            status = "waiting"
            client_datas_ofstatus = get_data_status(client_data, status)
            if len(client_datas_ofstatus) == 0:
                print(f"NO {status.upper()} LOAN OUTSTANDING")
            else:
                print("CUSTOMER'S WAITING LOAN ARE : ")
                print(client_datas_ofstatus)

        elif ch == 3:
            status = "open"
            client_datas_ofstatus = get_data_status(client_data, status)
            if len(client_datas_ofstatus) == 0:
                print(f"NO {status.upper()} LOAN OUTSTANDING")
            else:
                print("CUSTOMER'S CURRENT LOAN ARE : ")
                print(client_datas_ofstatus)

        elif ch == 4:
            status = "expired"
            client_datas_ofstatus = get_data_status(client_data, status)
            if len(client_datas_ofstatus) == 0:
                print(f"NO {status.upper()} LOAN OUTSTANDING")
            else:
                print("CUSTOMER'S EXPIRED LOAN ARE : ")
                print(client_datas_ofstatus)

        elif ch == 5:
            status = "open"
            client_datas_ofstatus = get_data_status(client_data, status)
            if len(client_datas_ofstatus) == 0:
                print(f"NO {status.upper()} LOAN OUTSTANDING")
            else:
                print("CUSTOMER'S TOTAL LOAN AMOUNT IS -> ")
                print(client_datas_ofstatus)
                print()
                print("TOTAL LOAN AMOUNT GRANTED IS :", sum(
                    client_datas_ofstatus.loc[:, "Loan_amount"]))

        elif ch == 6:
            print("TOTAL DUE AMOUNT")
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
                    print("FOR CLIENT", client_id, " DUE AMOUNT IS ", sum_due)
                    total_due = total_due + sum_due
    #            print(client_ids_pre)

            print("\n TOTAL DUE : ", total_due)

        elif ch == 7:
            print("RECENT TRANSACTION : ")
            trans_data = pd.read_csv("Transaction_Database.csv")
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
            continue

    except ChildProcessError:
        print("Main Menu")
        continue

    except:
        print("TRY AGAIN !!")
        print("IF ANY PROBLEM CONTACT ADMIN")
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
