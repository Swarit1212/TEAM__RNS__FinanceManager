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
    plt.figure(figsize=(12, 7))
    palette = sns.color_palette("pastel")  # Use a pastel color palette
    bar_plot = sns.barplot(x='Category', y='Amount', data=category_summary, palette=palette)

    # Add plot title and labels
    plt.title("Total Spending by Category", fontsize=20, fontweight='bold')
    plt.xlabel("Category", fontsize=15)
    plt.ylabel("Total Amount Spent ($)", fontsize=15)

    # Rotate the category labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)

    # Add grid lines for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Annotate bars with their values
    for p in bar_plot.patches:
        bar_plot.annotate(f'${p.get_height():,.0f}', 
                          (p.get_x() + p.get_width() / 2., p.get_height()), 
                          ha='center', va='bottom', fontsize=10, 
                          color='black', 
                          xytext=(0, 5),  # Offset text position
                          textcoords='offset points')

    # Display the plot
    plt.tight_layout()  # Adjust layout for better fit
    plt.show()
