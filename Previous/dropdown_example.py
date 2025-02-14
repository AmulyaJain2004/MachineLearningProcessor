import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Dropdown Menu Example")
root.geometry("400x200")

# Label to display the selected option
label = tk.Label(root, text="Select an option from the dropdown", font=("Arial", 12))
label.pack(pady=20)

# Create a StringVar to hold the current selection
selected_option = tk.StringVar()
selected_option.set("Option 1")  # Set default value

# Define options for the dropdown
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create the OptionMenu widget
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=10)

# Add a button to display the selected option
def show_selection():
    label.config(text=f"You selected: {selected_option.get()}")

button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack(pady=10)

# Run the application
root.mainloop()
