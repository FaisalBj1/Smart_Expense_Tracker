from datetime import datetime
import json
# import tkinter as tk
# import os

# # Create the main window
# class ExpenseTracker:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Expense Tracker")
#         self.window.geometry("1000x600")
#         self.expenses = []
#         self.setup_gui()
    
#     def setup_gui(self):
#         # Create GUI elements here
#         pass
    
#     def add_expense(self):
#         # Implementation here
#         pass
    
#     def view_expenses(self):
#         # Implementation here
#         pass
    
#     def run(self):
#         self.window.focus_force()
#         self.window.lift()
#         self.window.mainloop()

# main function ...
def main():
    # app = ExpenseTracker()
    # app.run()

    print("=== Smart Expense Tracker ===")

    # Main menu loop ...
    while True:
        # Main menu ...
        print("\n--- Main Menu ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Monthly summary")
        print("5. Exit")

        # Get user choice ...
        print("---------------------")
        choice = input("Your choice: ")

        # Handle user choice ...
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            monthly_summary()
        elif choice == '5':
            print("Ending the program.")
            print("---------------------") 
            break
        else:
            print("Invalid choice! Please enter 1-5.")
        print("---------------------")
        
        break


#-----------------------------------------------------------------------------------------
# functions ...
def add_expense():
    # Get user input for expense details ...
    title = input("Enter expense title: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = datetime.now().strftime("%Y-%m-%d")
    # Create a new expense dictionary ...
    new_expense = {
        'Expense title': title,
        'Amount': amount,
        'Category': category,
        'Date': datetime.now().strftime("%d-%m-%Y")
    }

    # adding new expense to json file and creating it if not exist ...
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = [] # I don't think this is needed but just in case

    expenses.append(new_expense)

    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)
        
        
    print("Expense added successfully!")
    pass

def view_expenses():
    # try:
    #     with open("expenses.json", "r") as expenses_file:
    #         expenses = json.load(expenses_file)
    #         if not expenses:
    #             print("No expenses found.")
    #         else:
    #             for expense in expenses:
    #                 print(f"Title: {expense['Expense title']}, Amount: {expense['Amount']}, Category: {expense['Category']}, Date: {expense['Date']}")
    # except FileNotFoundError:
    #     print("No expenses file found. Please add an expense first.")
    pass   

def delete_expense():
    # Logic to delete an expense
    pass

def monthly_summary():
    # Logic to show monthly summary
    pass

if __name__ == "__main__":
    main()