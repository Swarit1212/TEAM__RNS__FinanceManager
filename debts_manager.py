import pandas as pd

# Load debts from the CSV file
def load_debts(file_path="data/debts.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Debt Name", "Total Amount", "Monthly Payment"])

# Save the updated debts DataFrame to the CSV file
def save_debts(df, file_path="data/debts.csv"):
    df.to_csv(file_path, index=False)

# Add a new debt to the CSV file
def add_debt(debt_name, total_amount, monthly_payment):
    if not isinstance(total_amount, (int, float)) or total_amount < 0:
        print("Total amount must be a non-negative number.")
        return
    if not isinstance(monthly_payment, (int, float)) or monthly_payment < 0:
        print("Monthly payment must be a non-negative number.")
        return

    debts = load_debts()
    # Create a new debt entry
    new_debt = pd.DataFrame({
        "Debt Name": [debt_name],
        "Total Amount": [total_amount],
        "Monthly Payment": [monthly_payment]
    })
    # Append the new debt to the existing ones
    updated_debts = pd.concat([debts, new_debt], ignore_index=True)
    # Save the updated debts to the CSV
    save_debts(updated_debts)
    print("Debt added successfully!")

# View all debts
def view_debts():
    debts = load_debts()
    print(debts)

# Example Usage
if __name__ == "__main__":  # Corrected the conditional check
    # Add a new debt
    add_debt("Car Loan", 15000, 300)
    # View all debts
    view_debts()
