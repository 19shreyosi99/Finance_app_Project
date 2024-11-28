from authentication.register import register_user
from authentication.login import login_user
from tracker.income_expense import add_transaction, view_transactions, delete_transaction
from tracker.budget import set_budget, view_budget, check_budget
from reports.financial_reports import generate_monthly_report, generate_yearly_report
from database.db_manager import check_and_create_tables

def main():
    print("Welcome to the Personal Finance Manager!")
    check_and_create_tables()
    
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register_user()
        
        elif choice == '2':
            user = login_user()
            if user:
                while True:
                    print(f"\nWelcome, {user}!")
                    print("1. Manage Transactions")
                    print("2. Manage Budgets")
                    print("3. View Transactions")
                    print("4. View Budgets")
                    print("5. Check Budgets")
                    print("6. Generate Reports")
                    print("7. Logout")
                    user_choice = input("Enter your choice: ")
                    
                    if user_choice == '1':
                        print("\nTransaction Management:")
                        print("1. Add Transaction")
                        print("2. Delete Transaction")
                        transaction_choice = input("Enter your choice: ")
                        
                        if transaction_choice == '1':
                            amount = float(input("Enter amount: "))
                            category = input("Enter category: ").lower()
                            transaction_type = input("Enter type (income/expense): ").lower()
                            add_transaction(user, amount, category, transaction_type)
                        
                        elif transaction_choice == '2':
                            print("Enter the date of the transaction to delete (YYYY-MM-DD):")
                            date = input("Enter the date (YYYY-MM-DD): ")
                            delete_transaction(user, date)
                    
                    elif user_choice == '2':
                        print("\nBudget Management:")
                        category = input("Enter category: ")
                        limit_amount = float(input("Enter budget limit: "))
                        set_budget(user, category, limit_amount)
                    
                    elif user_choice == '3':
                        view_transactions(user)
                    
                    elif user_choice == '4':
                        view_budget(user)
                    
                    elif user_choice == '5':
                        check_budget(user)
                    
                    elif user_choice == '6':
                        print("\nGenerate Reports:")
                        print("1. Monthly Report")
                        print("2. Yearly Report")
                        report_choice = input("Enter your choice: ")
                        
                        if report_choice == '1':
                            generate_monthly_report(user)
                        elif report_choice == '2':
                            generate_yearly_report(user)
                        else:
                            print("Invalid choice!")
                    
                    elif user_choice == '7':
                        print("Logging out...")
                        break
                    
                    else:
                        print("Invalid choice! Please try again.")
        
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()