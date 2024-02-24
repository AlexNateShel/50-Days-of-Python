# Create a function called 'save_emails'.
# This function takes not arguments but asks the user to input an email, and it saves the email in a CSV file.
# The user can input as many emails as they want.
# Once they hit "done", the function saves the emails and closes the file.
# Create another functionc called 'open_emails'.
# This function opens and reads the content of the CSV file.
# Each email requires its own line.
# Here is an example of how the emails must be saved:
# jj@gmail.com
# kate@yahoo.com
# and not like this:
# jj@gmail.comkate@yahoo.com

def save_emails():
    w = []
    while True:
        email = input('Enter a email or done when finished: ')
        w.append(email)
        if email == 'done':
            break
        with open('emails.csv', 'a') as f:
            f. write(email)
            f .write('\n')

def open_emails():
    with open('emails.csv', 'r') as f:
        return f.read()
    

save_emails
print(open_emails())
