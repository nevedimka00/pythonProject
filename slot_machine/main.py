import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
   print(" | ".join(row))

def get_payout(row,bet):
    elements = set(row)
    match len(elements) :
        case 1 : 
            e=next(iter(elements))
            match e:
                case '🍒' : return bet*3
                case '🍉' : return bet*4
                case '🍋' : return bet*5
                case '🔔' : return bet*10
                case '⭐' : return bet*50  
        case 2 : return bet
        case _ : return 0

def welcome():
    print("********************")
    print("Welcome to Slots")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐")
    print("********************")

def updateBalance(balance):
    if balance==0:
        answer = input("Would you like to update balance? y/n ")
        if answer.lower()=='y': return 100
        else:return balance
    else: return balance


def main():
    balance=100
    welcome()
    while balance>0:
        print(f"Current balance: {balance}")
        bet=input("Please enter your bet(q to exit): ")
        if bet.lower()=='q':break
        if bet.isdigit():
            bet=int(bet)
            if bet<=balance and bet>0 :
                balance-=bet
                row = spin_row()
                print_row(row) 
                payout = get_payout(row,bet)
                balance+=payout
                print(f"Your payout is {payout}") if payout>0 else print(f"Sorry, you have lost {bet}")    
            else:print(f"Please enter the bet between 0 and {balance+1} ")
        else: print("Please enter correct bet")   
        balance = updateBalance(balance)
    print(f"Thank you for playing! Your current balance is: {balance}")

if __name__=='__main__':
    main()

