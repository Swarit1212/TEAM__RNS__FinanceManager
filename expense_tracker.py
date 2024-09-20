import pandas as pd
import os
from datetime import datetime

# Load expenses from a CSV file. If the file doesn't exist, return an empty DataFrame.
def load_expenses(file_path="data/expenses.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

# Save the expenses DataFrame to a CSV file
def save_expenses(df, file_path="data/expenses.csv"):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)

# Function to add a new expense
def add_expense(category, amount, description=""):
    if not isinstance(amount, (int, float)):
        print("Error: Amount must be a number.")
        return
    
    expenses = load_expenses()
    date = datetime.now().strftime("%Y-%m-%d")
    new_expense = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Amount": [amount],
        "Description": [description]
    })
    updated_expenses = pd.concat([expenses, new_expense], ignore_index=True)
    save_expenses(updated_expenses)
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    expenses = load_expenses()
    if expenses.empty:
        print("No expenses recorded.")
    else:
        print(expenses.to_string(index=False))  # Print without row indices

# Example Usage
if __name__ == "__main__":
    # Add an example expense
    add_expense("Groceries", 50, "Weekly groceries")
    # View all expenses
    view_expenses()
