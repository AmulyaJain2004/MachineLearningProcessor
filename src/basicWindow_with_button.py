import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Basic Tkinter App")
root.geometry("1200x700")

# Add a label
label = tk.Label(root, text="Welcome to VisualML!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
def on_button_click():
    label.config(text="You clicked the button!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()