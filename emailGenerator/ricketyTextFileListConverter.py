def main():
    firstNameFile = "firstnamelist.txt"
    lastNameFile = "lastnamelist.txt"
    newFirstNameFile = "newfirstnamelist.txt"
    newLastNameFile = "newlastnamefile.txt"
    firstName = []
    lastName = []
    lastName = storeNames(lastNameFile)
    ##This takes a list and capitalizes the first letter of the names in the list.
    lastName = [lastName.capitalize() for lastName in lastName]
    rewriteList(lastName, newLastNameFile)
    
    

def displayFirstNames(file):
    infile = open(file, 'r')
    for line in infile:
        print(line[4:], end="")
    infile.close

##Stores names to a list. Edit this based on the list issues.
def storeNames(file):
    infile = open(file, 'r')
    a = []
    for line in infile:
        a.append(str.strip(line))
    infile.close()
    return a

##Takes the new list and stores that in a new text file with proper formatting.
def rewriteList(firstName, fileName):
    wordsToRewrite = firstName
    for i in range(len(wordsToRewrite)):
        wordsToRewrite[i] = wordsToRewrite[i] + "\n"
    outfile = open(fileName, 'w')
    outfile.writelines(wordsToRewrite)
    outfile.close()
    
        
    

main()
