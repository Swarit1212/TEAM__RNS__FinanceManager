import pandas as pd

# Load savings, debts, salary, and investments, then calculate net worth
def calculate_net_worth():
    # Load savings data (assets)
    try:
        assets = pd.read_csv("data/savings_goals.csv")
        if "Amount" not in assets.columns:
            print("Savings data is missing the 'Amount' column.")
            total_assets = 0
        else:
            total_assets = assets["Amount"].sum()
    except FileNotFoundError:
        total_assets = 0

    # Load debts data (liabilities)
    try:
        debts = pd.read_csv("data/debts.csv")
        if "Total Amount" not in debts.columns:
            print("Debts data is missing the 'Total Amount' column.")
            total_liabilities = 0
        else:
            total_liabilities = debts["Total Amount"].sum()
    except FileNotFoundError:
        total_liabilities = 0

    # Load salary data
    try:
        salary = pd.read_csv("data/income.csv")
        if "Amount" not in salary.columns:
            print("Salary data is missing the 'Amount' column.")
            total_salary = 0
        else:
            total_salary = salary[salary["Source"] == "Salary"]["Amount"].sum()
    except FileNotFoundError:
        total_salary = 0

    # Load investments data
    try:
        investments = pd.read_csv("data/investments.csv")
        if "Amount" not in investments.columns:
            print("Investments data is missing the 'Amount' column.")
            total_investments = 0
        else:
            total_investments = investments["Amount"].sum()
    except FileNotFoundError:
        total_investments = 0

    # Calculate total net worth
    net_worth = (total_assets + total_salary + total_investments) - total_liabilities
    print(f"Your net worth is: ${net_worth}")

# Example Usage
if __name__ == "__main__":
    # Calculate and print net worth
    calculate_net_worth()
