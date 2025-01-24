# Enhanced Bank Account Management System

# 🏦 Data Structures to Store Information
import time

account_holders = []  # Account names
balances = []  # Account balances
transaction_histories = []  # Account transaction logs
loans = []  # Account loan details

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03


def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")


def create_account():
    """Create a new account."""
    account_name = input("Enter your account name: ")

    if account_name in account_holders:
        print("Account already exists. Please choose a different name.")
    else:
        account_holders.append(account_name)
        balances.append(0)
        transaction_histories.append([])
        loans.append(0)
        print(f"Account for {account_name} created successfully!")


def deposit():
    my_name = input("Enter the name of the account: ")
    if my_name in account_holders:
        index = account_holders.index(my_name)
        my_deposit = input("Enter a deposit amount: ")
        if my_deposit.isdigit() and float(my_deposit) > 0:
            my_deposit = float(my_deposit)
            balances[index] += my_deposit
            transaction_histories[index].append(f"Deposited {my_deposit}, New Balance: {balances[index]}")
            print(f"Deposit successful! New balance: {balances[index]}")
        else:
            print("Deposit amount must be a positive number.")
    else:
        print(f"The account with name '{my_name}' does not exist.")



def withdraw():
    my_name = input("Enter the name of the account: ")
    if my_name in account_holders:
        index = account_holders.index(my_name)
        withdraw_sum = input("Enter a withdrawal amount: ")
        if withdraw_sum.isdigit() and 0 < float(withdraw_sum) <= balances[index]:
            withdraw_sum = float(withdraw_sum)
            balances[index] -= withdraw_sum
            transaction_histories[index].append(f"Withdrew {withdraw_sum}, New Balance: {balances[index]}")
            print(f"Withdrawal successful! Remaining balance: {balances[index]}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    else:
        print(f"The account with name '{my_name}' does not exist.")


def check_balance():
    my_name = input("Enter the name of the account: ")
    for my_name in account_holders:
        index = account_holders.index(my_name)
        print(f"The current balance of this account is: {balances[index]} leva.")
        print(f"💳 Current loan balance: {loans[index]} leva")
        break
    else:
        print(f"The account with name {my_name} does not exist.")


def list_accounts():
    index = 0
    if account_holders:
        for acc in account_holders:
            print(f"Name - {acc}")
            print(f"Balance - {balances[index]} leva")
            print(f"Loan: {loans[index]} leva")
            index += 1
    else:
        print("No accounts found.")

def transfer_funds():
    while True:
        sender_name = input("Enter the name of the account you want to get the money from: ")
        receiver_name = input("Enter the name of the account you want to transfer money to: ")
        is_first_found = False
        is_second_found = False
        for name in account_holders:
            if name == receiver_name:
                is_first_found = True
                break
        for name in account_holders:
            if name == sender_name:
                is_second_found = True
                break
        if is_first_found and is_second_found:
            sender_index = account_holders.index(sender_name)
            receiver_index = account_holders.index(receiver_name)
            amount = float(input("Enter the amount to transfer: "))
            if amount > 0 and balances[sender_index] >= amount:
                balances[sender_index] -= amount
                balances[receiver_index] += amount
                transaction_histories[sender_index].append(
                    f"Transferred {amount} to {receiver_name}, New Balance: {balances[sender_index]}"
                )
                transaction_histories[receiver_index].append(
                    f"Received {amount} from {sender_name}, New Balance: {balances[receiver_index]}"
                )

                print(f"Successfully transferred {amount} from {sender_name} to {receiver_name}.")
                break
            else:
                print("Insufficient balance or invalid amount. Please try again.")
        else:
            print("Enter valid names of the accounts.")


def view_transaction_history():
    account_name = input("Enter your account name: ")
    if account_name in account_holders:
        index = account_holders.index(account_name)
        print(f"\nTransaction History for {account_name}:")

        if transaction_histories[index]:
            for transaction in transaction_histories[index]:
                print(f"- {transaction}")
        else:
            print("No transactions found.")
    else:
        print("Account not found.")


def apply_for_loan():
    name = input("Enter the name of the account: ")
    if name in account_holders:
        index = account_holders.index(name)
        if loans[index] == 0:
            loan_amount = float(input(f"Enter loan amount (up to {MAX_LOAN_AMOUNT} leva): "))
            if 0 < loan_amount <= MAX_LOAN_AMOUNT:
                transaction_histories[index].append(f"Loan applied for {loan_amount},"
                                                    f" New Loan Balance: {loans[index]}")
                print(f"Loan of {loan_amount} approved for {name}.")
                loans.append(loan_amount)
            else:
                print(f"Loan amount must be between 0 and {MAX_LOAN_AMOUNT}.")
        else:
            print("Loan already applied.")
    else:
        print("Account not found.")
def repay_loan():
    def repay_loan():
        account_name = input("Enter account name: ")

        if account_name in account_holders:
            index = account_holders.index(account_name)

            if loans[index] > 0:
                repayment_amount = float(input(f"Enter repayment amount (Current loan: {loans[index]}): "))

                if repayment_amount > 0 and repayment_amount <= loans[index]:
                    loans[index] -= repayment_amount  # Deduct from the loan balance
                    balances[index] -= repayment_amount  # Deduct from the account balance
                    transaction_histories[index].append(f"Loan repaid {repayment_amount}, "
                                                        f"New Loan Balance: {loans[index]}")
                    print(f"Repayment of {repayment_amount} made. Remaining loan balance: {loans[index]}")
                else:
                    print("Repayment amount is invalid or exceeds loan balance.")
            else:
                print("No loan to repay.")
        else:
            print("Account not found.")


def identify_card_type():
    card_number = input("Enter a valid card number (16 integer numbers): ")
    if not card_number.isdigit() or len(card_number) != 16:
        print("Invalid card number.")
    else:

        if card_number.startswith("4"):
            print("This is VISA card.")
        elif card_number[:2] in [51, 52, 53, 54, 55]:
            print("This is MasterCard.")
        elif card_number[:2] in [34, 37]:
            print("This is AmericanExpress card.")
        else:
            print("We do not support this type of card.")


def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")
        time.sleep(2.1)



if __name__ == "__main__":
    main()
