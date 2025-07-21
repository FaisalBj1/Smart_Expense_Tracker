import tkinter as tk
from datetime import datetime
import json

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

    global expenses 
    expenses = []

    
    # Main menu loop ...
    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Monthly summary")
        print("5. Exit")

        choice = input("Your choice: ")

        if choice == '1':
            add_expense()

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            delete_expense()

        elif choice == '4':
            monthly_summary()

        elif choice == '5':
            print("Exiting the program.")
            print("---------------------")
            break

        print("---------------------")
        pass




# functions ...
def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({
        'Expence title': title,
        'Amount': amount,
        'Category': category,
        'Date': datetime.now().strftime("%d-%m-%Y")
    })
    print("Expense added to list successfully!")

    # adding new expense to json file and creating it if not exist...
    with open("notes.txt", "w") as expenses_file:
        json.dump(expenses, expenses_file, indent=4)
        print("Expense added to json successfully!")
        
    print("Current expenses:", expenses)
    pass

def view_expenses():
    # Logic to view expenses
    pass        
def delete_expense():
    # Logic to delete an expense
    pass
def monthly_summary():
    # Logic to show monthly summary
    pass
def exit():
    # Logic to show monthly summary
    pass

if __name__ == "__main__":
    main()