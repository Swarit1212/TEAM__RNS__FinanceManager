import pandas as pd

# Load budget data from CSV, or create an empty DataFrame if file is missing
def load_budget(file_path="data/budget.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Category", "Budget"])

# Save the updated budget data to a CSV file
def save_budget(df, file_path="data/budget.csv"):
    df.to_csv(file_path, index=False)

# Set a budget for a specific category
def set_budget(category, amount):
    if amount < 0:
        print("Budget amount must be non-negative.")
        return

    # Load the existing budget
    budget = load_budget()
    # If the category exists, update the budget, otherwise create a new entry
    if category in budget["Category"].values:
        budget.loc[budget["Category"] == category, "Budget"] = amount
    else:
        new_budget = pd.DataFrame({"Category": [category], "Budget": [amount]})
        budget = pd.concat([budget, new_budget], ignore_index=True)
    # Save the updated budget back to the CSV
    save_budget(budget)
    print(f"Budget for {category} set to {amount}.")

# Check how much has been spent compared to the budget for each category
def check_budget_status():
    # Load both the budget and expenses
    budget = load_budget()
    try:
        expenses = pd.read_csv("data/expenses.csv")
        if not all(col in expenses.columns for col in ["Category", "Amount"]):
            print("Expenses file is missing required columns.")
            return
    except FileNotFoundError:
        print("Expenses file not found. Please add expenses.")
        return

    # Check if there are no expenses
    if expenses.empty:
        print("No expenses to analyze.")
        return
    
    # Summarize total spending by category
    summary = expenses.groupby("Category")["Amount"].sum().reset_index()
    
    # Merge the budget with the summarized spending
    merged = pd.merge(budget, summary, on="Category", how="left").fillna(0)
    
    # Check each category for budget status
    for index, row in merged.iterrows():
        if row["Amount"] > row["Budget"]:
            print(f"Exceeded budget for {row['Category']}: Spent {row['Amount']}, Budget {row['Budget']}")
        else:
            print(f"Within budget for {row['Category']}: Spent {row['Amount']}, Budget {row['Budget']}")

# Example Usage
if __name__ == "__main__":  # Corrected the conditional check
    # Set budgets for categories
    set_budget("Groceries", 500)
    set_budget("Entertainment", 100)
    # Check the budget status based on current expenses
    check_budget_status()
