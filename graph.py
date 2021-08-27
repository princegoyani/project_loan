import matplotlib.pyplot as plt
import pandas as pd
from pay_shcd import loan_transaction
from datetime import date
principal = loan_transaction["Principal"]
bal_out = loan_transaction["Bal_out"]
emi = loan_transaction["EMI"]
mon_int = loan_transaction["Monthly Interest"]
# print("time", loan_transaction["DUE DATE"])
time = loan_transaction["DUE DATE"]


# graph_Data = pd.DataFrame([bal_out, principal, mon_int], index=time)

# plt.plot(graph_Data)

# plt.xticks(time)


# time = date(loan_transaction["DUE DATE"]).year
# print(time)
"""print(principal)
print("BAL_OUT", bal_out)
a = round(bal_out[1])
print(round(a))"""
# b = list(range(1000000, 10000000, 100000))
# print(b)
#print(bal_out.tail(1).values[0], type(bal_out.tail(1).values[0]))
plt.figure(figsize=(7, 5))
loan_amount = bal_out.head(1).values[0]
plt.plot(time, principal, color="r")
plt.plot(time, emi, color="g")
plt.plot(time, mon_int, color="yellow")
plt.grid(True)
emi = emi.loc[1]
# print(emi)
emi_round = round(emi,  - (len(str(emi)) - 1))
# print(emi_round)
emi_Start = str(emi_round)[0]
#print(emi_round / int(emi_Start))
emi_round_1 = emi_round + emi_round / int(emi_Start)
# print(emi_round_1)
plt.yticks(
    list(range(0, int(emi_round_1) + 1, int(emi_round / 10))))

# int(emi_round) + int(emi_round / 2)
plt.yscale("linear")
#
# plt.yticks(b)
# bal_out[0], bal_out.tail(1), principal))
# plt.yticks(list(range(1000000, 10000000, 2000000)))
# plt.ticklabel_format(useOffset=False)
plt.xlabel("Due DATES")
plt.ylabel("RUPESS")
plt.title("PAYMENT SCH GRAPH")
plt.legend(["PRICIPAL", "BAL_OUT", "MON_INTE"])


plt.show()
