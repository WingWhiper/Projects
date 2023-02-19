import tkinter as tk
from tkinter import filedialog


# Functions
def select_file():
    filename = filedialog.askopenfilename(title="Select INI File", filetypes=[("INI files", "*.ini")])
    print("Selected file:", filename)


# Setting up the main display window
root = tk.Tk()
root.title("INI File Editor")
root.geometry("400x300")

select_button = tk.Button(root, text="Select INI File", command=select_file)
select_button.pack(pady=20)

root.mainloop()
