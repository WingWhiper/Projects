#####################################################
# The goal is to create a file system for           #
# organizational purposes of class materials.       #
# We want a root folder with the semester term,     #
# format of [fall, summer, spring], and the year    #
# The root folder should then create sub folders    #
# for each class enrolled in for that semester      #
#####################################################
from pathlib import Path
from datetime import date, datetime

# Users should choose the semester though input
semesters = ['Fall', 'Spring', 'Summer']
current_date = date.today()
current_year = current_date.year
# If the current month is past November
# then we need the year folder to create
# a folder for the next year,
# since the next semester is after January 1st
if current_date.month >= 11:
    current_year += 1
# gets the users' choice for the semester
while True:
    try:
        set_semester = int(input('Enter the Semester: \n1. Fall\n2. Spring\n3. Summer\n')) - 1
        break
    except ValueError:
        print('Please enter a number between 1 -3')
# Get the amount of classes being taken for the loop to assign the file names
while True:
    try:
        num_classes = int(input('How many classes are you taking?\n'))
        break
    except ValueError:
        print('Please enter a number value only')
# this creates the main parent directory
path = Path(f'C:/Users/wingw/Desktop/{semesters[set_semester]}{current_year}')
path.mkdir(parents=True, exist_ok=True)
# this loops lets the user set up the folder names based on the amount of classes taken
while num_classes > 0:
    class_name = str(input('Please enter the name of your class: '))
    new_path = Path(f'{path}/{class_name}')
    new_path.mkdir(parents=True, exist_ok=True)
    num_classes -= 1
# Ideas to add:
# Automatically pull the folder names from class schedule
# Allow the user a way to delete the entire folder system
# Maybe some way to allow the user to fix typos in the app?
# Add an array of classes, then allow the user to select
# the class number, then assign the official name to the folder.
