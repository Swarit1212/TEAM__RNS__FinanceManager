import pandas as pd

# Calculate net worth based on assets (savings) and liabilities (debts)
def calculate_net_worth():
    # Load savings data
    try:
        assets = pd.read_csv("data/savings_goals.csv")
        if "Amount" not in assets.columns:
            print("Savings data is missing the 'Amount' column.")
            total_assets = 0
        else:
            total_assets = assets["Amount"].sum()
    except FileNotFoundError:
        # If no savings file, assume no assets
        total_assets = 0

    # Load debts data
    try:
        debts = pd.read_csv("data/debts.csv")
        if "Total Amount" not in debts.columns:
            print("Debts data is missing the 'Total Amount' column.")
            total_liabilities = 0
        else:
            total_liabilities = debts["Total Amount"].sum()
    except FileNotFoundError:
        # If no debts file, assume no liabilities
        total_liabilities = 0

    # Calculate net worth as assets minus liabilities
    net_worth = total_assets - total_liabilities
    print(f"Your net worth is: ${net_worth}")

# Example Usage
if __name__ == "__main__":  # Corrected the conditional check
    # Calculate and print net worth
    calculate_net_worth()
