from tkinter import filedialog, Tk, Listbox, Button, Label
import configparser


# Functions
def select_file():
    filename = filedialog.askopenfilename(title="Select INI File", filetypes=[("INI files", "*.ini")])
    print("Selected file:", filename)

    # Get the character name from the filename
    prefix, character = filename.split("_", 1)
    character = character[:-4]  # Remove the ".ini" file extension

    # Update the window title with the character name
    root.title(f"INI File Editor - {character}")

    return filename


# Get the config file's sections
def get_sections(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config.sections()


def load_ini_file(filename, section_listbox, options_listbox):
    # Delete any previous entries in the section_listbox and options_listbox
    section_listbox.delete(0, 'end')
    options_listbox.delete(0, 'end')

    # Read the INI file and populate the section_listbox with the sections
    config = configparser.ConfigParser()
    config.read(filename)
    sections = config.sections()

    # Set the current section to the first section in the list
    current_section = sections[0]

    # Populate the options_listbox with the options in the current section
    options = config.options(current_section)
    for option in options:
        options_listbox.insert('end', option)

    # Set up the section labels and their associated options lists
    section_labels = []
    option_lists = []
    for section in sections:
        # Create a label for the section
        label = Label(root, text=section, font=("TkDefaultFont", 12, "bold"), pady=10)
        label.grid(column=len(section_labels), row=0)

        # Create a listbox for the options in the section
        options = Listbox(root)
        option_lists.append(options)
        for option in config.options(section):
            options.insert('end', option)
        options.grid(column=len(section_labels), row=1)

        # Add the label and options list to the section_labels list
        section_labels.append(label)

    # Pack the section listbox and options listbox in the window
    section_listbox.pack(side='left', fill='both', expand=True)
    options_listbox.pack(side='left', fill='both', expand=True)

    # Select the first section in the list
    section_listbox.selection_set(0)

    # Update the options listbox with the options for the current section
    current_section = section_listbox.get('active')
    options_listbox.delete(0, 'end')
    for option in config.options(current_section):
        options_listbox.insert('end', option)


# Setting up the main display window
root = Tk()
section_listbox = Listbox(root)
options_listbox = Listbox(root)
root.title("INI File Editor")
root.geometry("400x300")

select_button = Button(root, text="Select INI File", command=lambda: load_ini_file(select_file(), section_listbox, options_listbox))
select_button.grid(column=0, row=0, pady=20)

root.mainloop()
