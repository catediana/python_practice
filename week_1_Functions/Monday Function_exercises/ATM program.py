# Initial global account balance
account_balance = 1000.00

def check_balance():
    """Displays the current account balance."""
    print(f"\n Current Balance: ${account_balance:.2f}")

def deposit_money():
    """Allows the user to deposit a positive amount of money."""
    global account_balance
    try:
        amount = float(input("\nEnter the amount to deposit: $"))
        if amount > 0:
            account_balance += amount
            print(f" Successfully deposited ${amount:.2f}")
            check_balance()
        else:
            print("Invalid amount. Deposit must be greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def withdraw_money():
    """Allows the user to withdraw money if sufficient funds exist."""
    global account_balance
    try:
        amount = float(input("\nEnter the amount to withdraw: $"))
        if amount <= 0:
            print(" Invalid amount. Withdrawal must be greater than zero.")
        elif amount > account_balance:
            print(" Transaction declined: Insufficient funds.")
            check_balance()
        else:
            account_balance -= amount
            print(f" Successfully withdrew ${amount:.2f}")
            check_balance()
    except ValueError:
        print(" Invalid input. Please enter a valid number.")

def main_menu():
    """Runs the main ATM system loop."""
    print("--- Welcome to the Python ATM Simulator ---")
    
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print(" Invalid selection. Please choose a valid menu number.")

# Run the program
if __name__ == "__main__":
    main_menu()
