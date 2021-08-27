from login import clientid
from main import transaction, Check_loan, notice, number_ofloan_ofaclinet, curr_format, new_loan, pay_now, pay_shcd
import os
# print()
a = 0
while a == 0:
    try:
        Check_loan()
        notice(clientid)
        print()
        print("\t\t*--------*-----------*--------*")
        print("\t\t|\t | MAIN MENU |        |")
        print("\t\t|\t *-----------*        |")
        print("\t\t|\t                      |")
        print("\t\t| 1.NEW LOAN                  |\n\t\t| 2.NO OF LOAN IS             |\n\t\t| 3.PREVIOUS TRANSACTION      |\n\t\t| 4.PAY YOUR CURRENT LOAN     |\n\t\t| 5.PAYMENT SCHEDULE FOR LOAN |\n\t\t| 6.LOGOUT                    |")
        print("\t\t|\t                      |")
        print("\t\t*-----------------------------*")
        print("PRESS 'q' TO RETURN TO MAIN MENU ANYWHERE IN THE PROGRAM!")

        ch = int(input("ENTER YOUR CHOICE : "))

        if ch == 1:

            print("NEW LOAN IS LOADING")
            print()
            # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
            # exec(open("new_loan.py").read())
            new_loan(clientid)
            continue
        elif ch == 2:
            print("NUMBER OF LOAN IS")
            # exec(open("no_of_loans.py").read())
            number_ofloan_ofaclinet(clientid)
            continue
        elif ch == 3:
            print("YOUR PREVIOUS TRANSACTION :")
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
                print()
                print("YOUR TOTAL NO. OF PAID AMOUNT IS : ",
                      curr_format(trans_am))
                print()

            continue
        elif ch == 4:

            print("Pay Now !")
            print()
            # exec(open("pay_now.py").read())
            pay_now(clientid)
            continue

        elif ch == 5:
            print("PAYMENT SCHEDULE")
            print()
            # exec(open("pay_shcd.py").read())
            pay_shcd(clientid)
            continue
        elif ch == 6:
            print("LOGGING OUT .....")
            print()
            print("Thank you For Visting !")
            print()
            raise ZeroDivisionError

        else:
            print("PLEASE RE ENTER YOUR CHOICE !!!")
            print()
            continue

    except ChildProcessError:  # used in q for returning to main menu
        print()
        continue

    except ZeroDivisionError:
        print()
        os.abort()

    except ModuleNotFoundError:
        print("INSTALL NECESSARY MODUALS !!! ")
        print("REQUIRED MODUAL :- 1) PANDAS 2) MATHPOTLIB")
        break
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
