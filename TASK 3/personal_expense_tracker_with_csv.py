# PROJECT 03: PERSONAL EXPENSE TRACKER WITH CSV
import csv
import os
from datetime import datetime
from collections import defaultdict
FILE = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]
# Create CSV file if missing
def create_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
# Load all expenses
def load_expenses():
    create_file()
    with open(FILE, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
# Save a new expense
def save_expense(row):
    create_file()
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(row)
# Add expense
def add_expense():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Try again.")
    categories = ["Food", "Travel", "Study", "Bills", "Fun"]
    print("\nCategories:", ", ".join(categories))
    category = input("Enter category: ").strip().title()
    if category not in categories:
        print("Invalid category! Using Other.")
        category = "Other"
    description = input("Enter description: ").strip()
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Enter a valid amount.")
    row = {
        "date": date,
        "category": category,
        "description": description,
        "amount": str(amount)
    }
    save_expense(row)
    print("Expense saved successfully!")
# Display expenses
def view_expenses(rows):
    if not rows:
        print("No expenses found.")
        return
    print("\nDATE         CATEGORY     DESCRIPTION       AMOUNT")
    print("-" * 60)
    for r in rows:
        print(
            f"{r['date']:<12}"
            f"{r['category']:<13}"
            f"{r['description']:<19}"
            f"{float(r['amount']):.2f}"
        )
# Filter expenses
def filter_expenses():
    rows = load_expenses()
    print("\n1. Filter by category")
    print("2. Filter by month")
    choice = input("Choose filter: ").strip()
    if choice == "1":
        category = input("Enter category: ").strip().lower()
        filtered = [
            r for r in rows
            if r["category"].lower() == category
        ]
    elif choice == "2":
        month = input("Enter month (YYYY-MM): ").strip()
        try:
            datetime.strptime(month, "%Y-%m")
            filtered = [
                r for r in rows
                if r["date"].startswith(month)
            ]
        except ValueError:
            print("Invalid month format.")
            return
    else:
        print("Invalid choice.")
        return
    view_expenses(filtered)
# Expense summary
def summary():
    rows = load_expenses()
    if not rows:
        print("No expenses available.")
        return
    totals = defaultdict(float)
    for r in rows:
        totals[r["category"]] += float(r["amount"])
    print("\n===== CATEGORY SUMMARY =====")
    for category, total in sorted(totals.items()):
        print(f"{category}: Rs. {total:.2f}")
    grand_total = sum(totals.values())
    biggest = max(rows, key=lambda r: float(r["amount"]))
    print("\nGrand Total: Rs.", round(grand_total, 2))
    print("Biggest Expense:", biggest["description"])
    print("Biggest Amount: Rs.", biggest["amount"])
# Main menu
def main():
    create_file()
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Expense Summary")
        print("5. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses(load_expenses())
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Select 1 to 5.")
if __name__ == "__main__":
    main()
