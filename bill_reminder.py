import pandas as pd
from datetime import datetime

# Add a new bill to the CSV file
def add_bill(bill_name, due_date, amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        print("Amount must be a non-negative number.")
        return

    try:
        # Load the existing bills
        bills = pd.read_csv("data/bills.csv")
    except FileNotFoundError:
        # If the file doesn't exist, create an empty DataFrame
        bills = pd.DataFrame(columns=["Bill Name", "Due Date", "Amount"])

    # Create a new bill entry
    new_bill = pd.DataFrame({
        "Bill Name": [bill_name],
        "Due Date": [due_date],
        "Amount": [amount]
    })
    # Append the new bill to the existing ones
    bills = pd.concat([bills, new_bill], ignore_index=True)
    # Save the updated bills to the CSV
    bills.to_csv("data/bills.csv", index=False)
    print("Bill added successfully!")

# Check for any bills that are due today or earlier
def check_due_bills():
    try:
        # Load the bills from the CSV
        bills = pd.read_csv("data/bills.csv")
    except FileNotFoundError:
        print("No bills found.")
        return
    
    # Get today's date
    today = datetime.now().strftime("%Y-%m-%d")
    # Convert Due Date to datetime for comparison
    bills["Due Date"] = pd.to_datetime(bills["Due Date"], errors='coerce')
    due_bills = bills[bills["Due Date"] <= today]
    
    # Check if any bills are due
    if due_bills.empty:
        print("No bills are due today.")
    else:
        print("Due Bills:")
        print(due_bills)

# Example Usage
if __name__ == "__main__":  # Corrected the conditional check
    # Add a new bill
    add_bill("Electricity", "2024-09-20", 100)
    # Check for due bills
    check_due_bills()
