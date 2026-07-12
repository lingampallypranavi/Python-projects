# Expense Tracker Project

expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Expense
    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added successfully!")

    # View Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")

        else:
            print("\nExpense List:")
            for i, amount in enumerate(expenses, start=1):
                print(f"{i}. ₹{amount}")

    # Total spent
    elif choice == "3":
        total = 0

        for amount in expenses:
            total = total + amount

        print(f"\nTotal Spent: ₹{total}")

    # Exit
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")