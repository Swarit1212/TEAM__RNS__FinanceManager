import pandas as pd

# Load investment data from CSV or create an empty DataFrame if the file doesn't exist
def load_investments(file_path="data/investments.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Investment Name", "Amount", "Date", "Return"])

# Save the investments DataFrame to a CSV file
def save_investments(df, file_path="data/investments.csv"):
    df.to_csv(file_path, index=False)

# Function to add a new investment
def add_investment(investment_name, amount, date):
    investments = load_investments()
    new_investment = pd.DataFrame({
        "Investment Name": [investment_name],
        "Amount": [amount],
        "Date": [date],
        "Return": [0]  # Default return is 0 when the investment is made
    })
    updated_investments = pd.concat([investments, new_investment], ignore_index=True)
    save_investments(updated_investments)
    print("Investment added successfully!")

# Function to add a return to an existing investment
def add_return(investment_name, return_amount):
    investments = load_investments()
    if investment_name in investments["Investment Name"].values:
        investments.loc[investments["Investment Name"] == investment_name, "Return"] += return_amount
        save_investments(investments)
        print(f"Return of ${return_amount} added to {investment_name}.")
        # Store the return as income in the income file
        save_return_to_income(return_amount)
    else:
        print("Investment not found.")

# Function to view all investments
def view_investments():
    investments = load_investments()
    if investments.empty:
        print("No investments found.")
    else:
        print(investments)

# Function to store returns in the income file
def save_return_to_income(return_amount, file_path="data/income.csv"):
    try:
        income_data = pd.read_csv(file_path)
    except FileNotFoundError:
        income_data = pd.DataFrame(columns=["Source", "Amount"])

    # Add return as income
    new_income = pd.DataFrame({"Source": ["Investment Return"], "Amount": [return_amount]})
    updated_income = pd.concat([income_data, new_income], ignore_index=True)
    updated_income.to_csv(file_path, index=False)
    print("Return added to income file.")

# Example Usage
if __name__ == "__main__":
    # Add a new investment
    add_investment("Stocks", 1000, "2024-09-20")
    # Add a return to an investment
    add_return("Stocks", 100)
    # View all investments
    view_investments()
