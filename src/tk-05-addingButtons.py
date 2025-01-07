import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("VisualML")

label = tk.Label(root,
                 text = "Hello!",
                 font = ('Arial', 18))
label.pack(padx= 10, pady = 30)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack()

root.mainloop()