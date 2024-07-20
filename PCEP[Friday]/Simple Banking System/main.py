from Bank import *
def main() -> None:
    bank = Bank("Chase Bank")
    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Details")
        print("5. Exit")

        choice = input("Choose an option")

        if choice == "1":
            account_number = input("Enter an Account Number: ")
            account_holder = input("Enter Account Holder Name: ")
            if bank.create_account(account_number,account_holder):
                print(f"Account for {account_holder} created successfully.")
            else:
                print("Account creation failed. Account Number already exists.")
        elif choice == "2":
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Deposit: "))
            if bank.deposit(account_number, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed. Check account number and amount.")
        
        elif choice == "3":
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Withdraw: "))
            if bank.withdraw(account_number, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed. Check account number and balance.")
        
        elif choice == "4":
            account_number = input("Enter Account Number: ")
            print(bank.display_account_details(account_number))
        
        elif choice == "5":
            print("Exiting Banking System.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()