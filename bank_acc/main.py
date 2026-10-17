
def main():
    balance = 0
    is_running = True
    warning = "Please enter the correct option!"
    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdrawal")
        print("4.Exit Program")
        user_option = input("Please choose your option: ")
        match user_option:
            case "1" : show_balance(balance)
            case "2" : balance = deposit(balance)
            case "3" : balance = withdrawal(balance)
            case "4" : 
                print("GoodBye!")
                is_running=False
            case _ : 
                print("--------------------------")
                print(warning)
                print("--------------------------")

def show_balance(balance):
    print("--------------------------")
    print(f"Your Balance is {balance}")
    print("--------------------------")

def deposit(balance):
    print("--------------------------")
    user_deposit = input("Please enter your deposit ")
    if user_deposit.isdigit():
        value=float(user_deposit)
        if(value>0):return balance+value 
        else:
            print("Value must be more than 0") 
            return balance
    else : 
        print("Please enter a positive number")
        return balance

def withdrawal(balance):
    print("--------------------------")
    user_withdrawal = input("Please enter your withdrawal ")
    if user_withdrawal.isdigit():
        value = float(user_withdrawal)
        if balance>=value:return balance-value
        else: 
            print("Negative balance is not allowed")
            return balance
    else : 
        print("Please enter a positive number")
        return balance


if __name__=="__main__":
    main()


