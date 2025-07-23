import csv
from datetime import datetime

filename = 'expenses.csv'

def add_expense():
    # Ask user for details
    date = input("📅 Enter date (YYYY-MM-DD): ")
    amount = input("💰 Enter amount (e.g., 250.00): ")
    category = input("📂 Enter category (e.g., Food, Transport, Rent): ")
    note = input("📝 Enter a short note (optional): ")

    # Write to CSV
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    
    print("✅ Expense saved successfully!")

# Run the function
add_expense()
