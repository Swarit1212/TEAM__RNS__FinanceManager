import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a spending report visualized as a bar plot
def generate_spending_report():
    try:
        # Load expenses from CSV
        expenses = pd.read_csv("data/expenses.csv")
    except FileNotFoundError:
        print("No expenses found.")
        return
    
    # If there are no expenses, exit the function
    if expenses.empty:
        print("No expenses to report.")
        return
    
    # Summarize spending by category
    category_summary = expenses.groupby('Category')['Amount'].sum().reset_index()

    # Print summary in terminal
    print("\nSpending by Category:")
    print(category_summary)
    
    # Create a bar plot to visualize spending by category
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Amount', data=category_summary, palette='viridis')
    
    # Add plot title and labels
    plt.title("Total Spending by Category", fontsize=16)
    plt.xlabel("Category", fontsize=14)
    plt.ylabel("Total Amount Spent", fontsize=14)
    
    # Rotate the category labels for better readability (in case they are long)
    plt.xticks(rotation=45, ha='right')
    
    # Display the plot
    plt.tight_layout()  # Adjust layout for better fit
    plt.show()