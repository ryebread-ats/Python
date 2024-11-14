#Python banking program

def show_balance(balance):
    print(f"Balance: ${balance:.2f}")

def deposit():
    amount = float(input("Please enter the amount you would like to deposit: "))
    if amount > 0:
        print(f"You have deposited: ${amount}")
        return amount
    else:
        print("Invalid deposit amount.")
        return 0 

def withdraw(balance):
    amount = float(input("Please enter the amount you would like to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Invalid withdraw amount.")
        return 0
    else:
        print(f"You have withdrawn: ${amount}")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------")
        print("Banking Program")
        print("----------")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("----------")
        choice = input("Enter your choice(1-4): ")
        print("----------")
        if choice == "1":   #show balance
            show_balance(balance)
        elif choice == "2": #deposit
            balance += deposit()
            print(f"Updated Balance: ${balance:.2f}")
        elif choice == "3": #withdraw
            balance -= withdraw(balance)
            print(f"Remaining Balance: ${balance:.2f}")
        elif choice == "4": #exit
            is_running = False
            print("Exiting...")
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()