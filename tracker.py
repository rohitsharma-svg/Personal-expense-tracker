import csv

# Step 1: Create a new CSV file with headers
filename = 'expenses.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Amount', 'Category', 'Note'])

print("✅ 'expenses.csv' created with headers: Date, Amount, Category, Note")
