from numpy.testing._private.utils import break_cycles
import pandas as pd
from main import due_Date_cal, move_tomainmenu
import datetime
from dateutil.relativedelta import relativedelta
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


client_data = pd.read_csv("Client Database.csv",
                          sep=",", header=0)

waiting_Database = pd.DataFrame(columns=client_data.columns)
row = 1
for i in client_data.index:
    if client_data.loc[i, "Status"].lower() == "waiting":
        waiting_Database.loc[row] = client_data.loc[i, :]
        row = row + 1
if len(waiting_Database) == 0:
    print("NO Waiting LOANS !")

else:

    while True:
        print(waiting_Database)
        try:
            cho_toapp = input(
                "ENTER INDEX YOU WANT TO APPROVE OR DENY FOR : ")
            move_tomainmenu(cho_toapp, "emp")
            cho_toapp = int(cho_toapp)

            if cho_toapp in waiting_Database.index.tolist():
                ans = input(
                    "*************""\n* 1)APPROVE *\n* 2)DENY    *\n""*************""\nENTER YOUR CHOICE : ")
                move_tomainmenu(ans, "emp")

                loan_id_verifi = waiting_Database.loc[cho_toapp, "loan_id"]

                if ans == "1" or ans.lower() == "approve":
                    # print(ans, "1")
                    for j in client_data.index:
                        if loan_id_verifi == client_data.loc[j, "loan_id"]:
                            # print("match")
                            # due_date_ini = client_data.loc[j, "Due_date"]
                            time = client_data.loc[j, "for YEAR"]
                            Starting_date = datetime.date.today()
                            ending_date = Starting_date + \
                                relativedelta(years=time)
                            due_date_ini = Starting_date + \
                                relativedelta(months=1)
                            # due_date = due_Date_cal(due_date_ini)
                            client_data.loc[j, "Starting_date"] = Starting_date
                            client_data.loc[j, "Ending_date"] = ending_date
                            client_data.loc[j, "Due_date"] = due_date_ini
                            client_data.loc[j, "Status"] = "open"
                            waiting_Database = waiting_Database.drop(
                                index=cho_toapp)
                            break
                    break
                elif ans == "2" or ans.lower() == "denide":
                    for k in client_data.index:
                        if loan_id_verifi == client_data.loc[k, "loan_id"]:
                            # print("HERE", loan_id_verifi)
                            client_data = client_data.drop(index=k)
                            waiting_Database = waiting_Database.drop(
                                index=cho_toapp)
                            break
                    break

                else:
                    print("ENTER VALID !!!")
                    continue

                # print("HERE")

            else:
                print("ENTER VALID")
                continue

        except ValueError:
            print("ENTER VALID !")
            continue

    # print(client_data)
    client_data.to_csv("Client Database.csv", index=False)
    # print(waiting_Database)
