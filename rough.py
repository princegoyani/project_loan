import datetime
a = int("$2323")


"""
#print(datetime.datetime.strptime("2008-04-04", "%y-%m-%d"))
Starting_date = datetime.date.fromisoformat("2021-09-25")
print(datetime.date.today().year)
due_months = (datetime.date.today().year - Starting_date.year) * \
    12 + (datetime.date.today().month - Starting_date.month)
print(due_months)"""
"""import pandas as pd

client_data = pd.read_csv("Client Database.csv",
                          sep=",", header=0)
cerdit_score = 0
sansacition_amount = 0
status_ofloan = "waiting"
clientid = 109
typeofloan = "bussniess"
int_rate = 6
principal = 100000000
time = 10
print(client_data)
last_index = client_data.tail(1).index[0]
print(last_index)
print(client_data.columns)
new_loandata = [111, cerdit_score, typeofloan,
                status_ofloan,  int_rate, principal, sansacition_amount, time]

client_data.loc[10] = new_loandata

print(client_data)
client_data.to_csv(path_or_buf="Client Database.csv",
                   sep=",", index=False, mode="w")
"""
