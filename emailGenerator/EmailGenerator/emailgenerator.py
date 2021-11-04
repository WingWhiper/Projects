def main():
    
    # Files needed to make the list
    first_name_file = "newfirstnamelist.txt"
    last_name_file = "newlastnamefile.txt"
    new_email_list_file = "newemaillist.txt"

    # variables to store names in
    email_hosts = ["yahoo.com", "gmail.com", "hotmail.com"]
    emails_to_generate = 0

    # Ask the user how many emails to generate
    while 0 >= emails_to_generate <= 100000:
        print("Please Enter a number above zero and below a hundred thousand")
        try:
            emails_to_generate = int(input("How many emails do you want to make?"))
        except ValueError:
            print("You did not enter a numeric value")
            emails_to_generate = 0

    # Adding items to the names lists.
    first_names = store_names(first_name_file)
    last_names = store_names(last_name_file)
    # Makes 100 random email addresses
    new_emails = generate_emails(first_names, last_names, email_hosts, emails_to_generate)
    # Store those emails in a file
    write_to_text_file(new_emails, new_email_list_file)


def store_names(file):
    # Takes in a file, then stores that file to a list removing newline tags.
    infile = open(file, 'r')
    a = []
    for line in infile:
        a.append(str.strip(line))
    infile.close()
    return a


def generate_emails(fn, ln, eh, te):
    import random
    # These values assign first names, last names, email hosts, and the total emails to generate.
    fn = fn
    ln = ln
    eh = eh
    te = te
    group = "".join(random.choice(fn) + random.choice(ln) + str(random.randint(100, 999)) + "@"
                    + random.choice(eh) + "\n" for _ in range(te))
    return group


def write_to_text_file(ne, fn):
    # Gives the new emails a variable to use to write the emails to a text file.
    text_to_write = ne
    # PyCharm suggested changing in to _ here. Need to understand why
    for _ in text_to_write:
        text_to_write = text_to_write + "\n"
    outfile = open(fn, 'w')
    outfile.writelines(text_to_write)
    outfile.close()


main()
