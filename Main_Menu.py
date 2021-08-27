from numpy.lib.function_base import _quantile_ureduce_func
from login import clientid
from main import transaction, Check_loan
import os
# print()
a = 0
while a == 0:
    Check_loan()
    try:
        exec(open("notics.py").read())
        print("PRESS 'q' TO RETURN TO MAIN MENU ANYWHERE IN THE PROGRAM !")
        print("*******************************")
        print("* 1.NEW LOAN                  *\n* 2.NO OF LOAN IS             *\n* 3.PREVIOUS TRANSACTION      *\n* 4.PAY YOUR CURRENT LOAN     *\n* 5.PAYMENT SCHEDULE FOR LOAN *\n* 6.LOGOUT                    *")
        print("*******************************")
        ch = int(input("ENTER YOUR CHOICE : "))

        if ch == 1:

            print("NEW LOAN IS LOADING")
            print()
            # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
            exec(open("new_loan.py").read())
            continue
        elif ch == 2:
            print("NO OF LOANS IS")
            print()
            exec(open("no_of_loans.py").read())
            continue
        elif ch == 3:
            print("YOUR PREVIOUS TRANSACTION ")
            print()

            # exec(open("transaction_history.py").read())
            trans = transaction(clientid)
            trans_hist = trans[0]
            trans_am = trans[1]

            if len(trans_hist) == 0:
                print("NO PAYMENT TILL !!!")
                print()
            else:
                print(trans_hist)
                print("YOUR TOTAL NO. OF PAID AMOUNT IS : ", trans_am)
                print()

            continue
        elif ch == 4:

            print("Pay Now !")
            print()
            exec(open("pay_now.py").read())
            continue

        elif ch == 5:
            print("PAYMENT SCHEDULE")
            print()
            exec(open("pay_shcd.py").read())
            continue
        elif ch == 6:
            print("LOGGING OUT .....")
            print()
            print("Thank you For Visting !")
            print()
            # KeyError
            raise ZeroDivisionError

        else:
            print("PLEASE RE ENTER YOUR CHOICE !!!")
            print()
            continue
    except ZeroDivisionError:
        print("LOG OUT !")
        print()
        os.abort()
        break
    except ChildProcessError:
        print("MAIN MENU")
        print()
        continue
    except:

        print("INVALID!!!")
        print()
        print(" IF ANY PROMBLEM PLEASE CONTACT BANK !!! ")
        print()
        continue

"""
    elif ch == 6:
        print("TOTAL NO OF INSTALMENTS IS")
    elif ch == 7:
        print(" TOTAL AMOUNT IS")
    elif ch == 8:
        print(" YOUR PAID AMOUNT IS ")
    elif ch == 9:
        print("YOUR UNPAID AMOUNT IS")
    elif ch == 10:
        print(" YOUR REMAINING INSTALMENTS")
    elif ch == 11:
        print(" YOUR NEXT PAYMENT  IS ")
    elif ch == 12:
        print("YOUR NEXT PAYMENT DATE IS ")
    elif ch == 13:
        print("LAST DATE FOR PAYING  INSTALMENT OF THIS MONTH IS ")

    elif ch == 14:
        pass
    elif ch == 15:
        print("TIME ALLOTED FOR LOAN COMPLETION (IN YEARS) IS :")

    else:
        print("PLZ REENTER YOUR CHOICE !!!")
        continue
    break
"""
