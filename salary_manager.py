import pandas as pd

# Load salary data from CSV or create a new DataFrame if the file doesn't exist
def load_salary(file_path="data/salary.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Salary"])

# Save the salary DataFrame to a CSV file
def save_salary(salary, file_path="data/salary.csv"):
    df = pd.DataFrame({"Salary": [salary]})
    df.to_csv(file_path, index=False)

# Function to input and save salary
def input_salary():
    salary = float(input("Enter your salary: "))
    save_salary(salary)
    print("Salary saved successfully!")

# Function to view salary
def view_salary():
    salary_data = load_salary()
    if salary_data.empty:
        print("No salary data found.")
    else:
        print(f"Your salary is: ${salary_data['Salary'].iloc[0]}")
