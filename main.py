# python banking system

def show_balance(balance):
    print("****************************************")
    print(f"   your balance is ksh {balance:.2f}   ")
    ("*********************************************")


def deposit():
    amount=float(input('enter an amount to be deposited: '))
    if amount <=0:
        print("**********************************")
        print('    thats not a valid amount      ')
        print("**********************************")
        return 0
    else:
        return amount


def withdraw(balance):
    amount=float(input("enter amount to be withdrawn: "))

    if amount> balance:
        print("insufficient funds ")
        return 0
    elif amount <= 0:
        print("**********************************")
        print("  amount must be greater than 0 " )
        print("**********************************")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("************************")
        print("    Banking Program     ")
        print("************************")

        print("1.show balance")
        print("2.Make a deposit")
        print("3.make a withdraw")
        print("4.exit")
        print("************************")

        choice=input("enter your choice 1-4: ")

        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance += deposit()
        elif choice=='3':
            balance -= withdraw(balance)
        elif choice=='4':
            is_running=False
        else:
            print("**********************************")
            print("    That is not a valid choice    ")
            print("**********************************")

    print("**********************************")
    print("    thank you have a nice day")
    print("**********************************")


if __name__=='__main__':
    main()