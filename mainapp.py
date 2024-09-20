import sys
from expense_tracker import add_expense, view_expenses
from budget_manager import set_budget, check_budget_status
from bill_reminder import add_bill, check_due_bills
from debts_manager import add_debt, view_debts
from net_worth import calculate_net_worth
from reports import generate_spending_report
from salary_manager import input_salary, view_salary
from investment_manager import add_investment, add_return, view_investments
def display_menu():
    print("\n===== Personal Finance Manager =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Budget")
    print("4. Check Budget Status")
    print("5. Add Bill")
    print("6. Check Due Bills")
    print("7. Add Debt")
    print("8. View Debts")
    print("9. Calculate Net Worth")
    print("10. Generate Spending Report")
    print("11. Input Salary")
    print("12. View Salary")
    print("13. Add Investment")
    print("14. Add Return on Investment")
    print("15. View Investments")
    print("16. Exit")
    print("====================================")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-16): ")
        
        try:
            if choice == '1':
                # Add Expense
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))
                description = input("Enter description (optional): ")
                add_expense(category, amount, description)
            
            elif choice == '2':
                # View Expenses
                view_expenses()
            
            elif choice == '3':
                # Set Budget
                category = input("Enter budget category: ")
                amount = float(input("Enter budget amount: "))
                set_budget(category, amount)
            
            elif choice == '4':
                # Check Budget Status
                check_budget_status()
            
            elif choice == '5':
                # Add Bill
                bill_name = input("Enter bill name: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                amount = float(input("Enter bill amount: "))
                add_bill(bill_name, due_date, amount)
            
            elif choice == '6':
                # Check Due Bills
                check_due_bills()
            
            elif choice == '7':
                # Add Debt
                debt_name = input("Enter debt name: ")
                total_amount = float(input("Enter total debt amount: "))
                monthly_payment = float(input("Enter monthly payment: "))
                add_debt(debt_name, total_amount, monthly_payment)
            
            elif choice == '8':
                # View Debts
                view_debts()
            
            elif choice == '9':
                # Calculate Net Worth
                calculate_net_worth()
            
            elif choice == '10':
                # Generate Spending Report
                generate_spending_report()

            elif choice == '11':
            # Input Salary
                input_salary()
        
            elif choice == '12':
                # View Salary
                view_salary()
            
            elif choice == '13':
            # Add Investment
                investment_name = input("Enter investment name: ")
                amount = float(input("Enter investment amount: "))
                date = input("Enter investment date (YYYY-MM-DD): ")
                add_investment(investment_name, amount, date)

            elif choice == '14':
            # Add Return on Investment
                investment_name = input("Enter investment name: ")
                return_amount = float(input("Enter return amount: "))
                add_return(investment_name, return_amount)
        
            elif choice == '15':
            # View Investments
                view_investments()
        
            elif choice == '16':
            # Exit
                print("Exiting... Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
    
        except ValueError:
            print("Invalid input. Please enter numeric values where required.")

if __name__ == "__main__":  # Corrected the conditional check
    main()
