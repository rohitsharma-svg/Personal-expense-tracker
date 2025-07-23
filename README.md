Personal Expense Tracker

Hi! This is a simple Python project I built to track my daily expenses.  
It helps me keep an eye on where my money goes — nothing fancy, just straightforward and useful.


 What It Does

- You can add your daily expenses (date, amount, category, note).
- It saves everything in a CSV file.
- You can view a summary later (like total spend, etc.)
- It's beginner-friendly and easy to customize.



 Tools Used

- Python 3
- CSV for data storage
- (Optional) Matplotlib or Seaborn for graphs later on



 Project Structure

Personal-expense-tracker/
├── add_expense.py # Adds a new expense entry
├── tracker.py # Creates the CSV file with headers
├── summary.py # Will show total/summary (work in progress)
├── expenses.csv # Your actual data gets saved here



 How to Run

1. Clone the repo  
   git clone https://github.com/rohitsharma-svg/Personal-expense-tracker.git
   cd Personal-expense-tracker
2. First time only – run this to create the CSV file:
   python tracker.py
3. To add an expense:
   python add_expense.py
4. To view summary (coming soon):
   python summary.py   
