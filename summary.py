import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
df = pd.read_csv("expenses.csv")

# Step 2: Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")

# Step 3: Calculate total expense
total_expense = df['Amount'].sum()
print(f"\n💰 Total Expense: ₹{total_expense:.2f}\n")

# Step 4: Group by Category
category_summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
print("📊 Category-wise Expense Summary:\n")
print(category_summary)

# Step 5: Plot a pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_summary, labels=category_summary.index, autopct="%1.1f%%", startangle=140)
plt.title("Expense Distribution by Category")
plt.axis('equal')
plt.tight_layout()
plt.show()
