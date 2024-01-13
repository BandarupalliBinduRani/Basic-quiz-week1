class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for expense in self.expenses:
                print(f"{expense['category']}: ${expense['amount']}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")


def get_valid_input(prompt, input_type):
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = get_valid_input("Enter your choice (1-4): ", str)

        if choice == '1':
            category = input("Enter expense category: ")
            amount = get_valid_input("Enter expense amount: ", float)
            tracker.add_expense(category, amount)

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            tracker.total_expenses()

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
