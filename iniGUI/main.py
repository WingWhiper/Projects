import tkinter as tk
from tkinter import filedialog


# Functions
def select_file():
    filename = filedialog.askopenfilename(title="Select INI File", filetypes=[("INI files", "*.ini")])
    print("Selected file:", filename)

    # Get the character name from the filename
    prefix, character = filename.split("_", 1)
    character = character[:-4]  # Remove the ".ini" file extension

    # Update the window title with the character name
    root.title(f"INI File Editor - {character}")


# Setting up the main display window
root = tk.Tk()
root.title("INI File Editor")
root.geometry("400x300")

select_button = tk.Button(root, text="Select INI File", command=select_file)
select_button.pack(pady=20)

root.mainloop()
