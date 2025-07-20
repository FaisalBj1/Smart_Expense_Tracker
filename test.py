# test file
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Basic GUI")
window.geometry("300x200")

# Add a simple label
label = tk.Label(window, text="Hello, this is a basic GUI!")
label.pack()

# Add a button
def button_click():
    label.config(text="Button was clicked!")

button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

# Start the GUI event loop
window.mainloop()