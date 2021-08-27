import matplotlib.pyplot as plt
import pandas as pd
from pay_shcd import loan_transaction
from datetime import date
principal = loan_transaction["Principal"]
bal_out = loan_transaction["Bal_out"]
mon_int = loan_transaction["Monthly Interest"]
print("time", loan_transaction["DUE DATE"])
time = loan_transaction["DUE DATE"]
# time = date(loan_transaction["DUE DATE"]).year
# print(time)
print(principal)
print("BAL_OUT", bal_out)
a = round(bal_out[1])
print(round(a))
b = list(range(1000000, 10000000, 100000))
print(b)
#plt.plot(time, principal, color="r")
#plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], b, color="g")
plt.plot(time, mon_int, color="yellow")
plt.yticks(b)
# bal_out[0], bal_out.tail(1), principal))
plt.yticks(list(range(1000000, 10000000, 2000000)))
# plt.ticklabel_format(useOffset=False)
plt.xlabel("Due DATES")
plt.ylabel("RUPESS")
plt.title("PAYMENT SCH GRAPH")
plt.legend(["PRICIPAL", "BAL_OUT", "MON_INTE"])


plt.show()
