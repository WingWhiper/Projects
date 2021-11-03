# Attempting to impliment a UI here.
from tkinter import *

#Varible reference to Tkinter
root = Tk()

#Assigning the menu to avariable
menu = Menu(root)
root.config(menu=menu)

#Creating a submenu with drop down choices
subMenu = Menu()
menu.add_cascade(label="File", menu=subMenu)

test_button = Button(root, text="Click to create emails")
test_button.bind("<Button-1>", main())
test_button.pack()

def main (event):
    
    #Files needed to make the list
    firstNameFile = "newfirstnamelist.txt"
    lastNameFile = "newlastnamefile.txt"
    newEmailListFile = "newemaillist.txt"

    #variables to store names in
    firstNames = []
    lastNames = []
    newemails = []
    emailHosts = ["yahoo.com", "gmail.com", "hotmail.com"]
    emailsToGenerate = 0

    #Ask the user how many emails to generate
    while emailsToGenerate <= 0 or emailsToGenerate >= 100000:
        print("Please Enter a number above zero and below a hundred thousand")
        try:
            emailsToGenerate = int(input("How many emails do you want to make?"))
        except ValueError:
            print("You did not enter a numeric value")
            emailsToGenerate = 0

    #Adding items to the names lists.
    firstNames = storeNames(firstNameFile)
    lastNames = storeNames(lastNameFile)
    #Makes 100 random email addresses
    newEmails = generateEmails(firstNames, lastNames, emailHosts, emailsToGenerate)
    #Store those emails in a file
    writeToTextFile(newEmails, newEmailListFile)

    

def storeNames(file):
    ##Takes in a file, then stores that file to a list removing newline tags.
    infile = open(file, 'r')
    a = []
    for line in infile:
        a.append(str.strip(line))
    infile.close()
    return a

def generateEmails(fn, ln, eh, te):
    import random
    #These values assign first names, last names, email hosts, and the total emails to generate.
    fn = fn
    ln = ln
    eh = eh
    te = te
    group="".join(random.choice(fn) + random.choice(ln) + str(random.randint(100, 999)) + "@" + random.choice(eh) + "\n" for _ in range(te))
    return group

def writeToTextFile(ne, fn):
    #Gives the new emails a variable to use to write the emails to a text file.
    textToWrite = ne
    for i in textToWrite:
        textToWrite = textToWrite + "\n"
    outfile = open(fn, 'w')
    outfile.writelines(textToWrite)
    outfile.close()

root.mainloop()
main()

    
