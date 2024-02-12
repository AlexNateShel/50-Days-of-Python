# Write a function called 'email_validator' that takes a list of emails and checks if the emails are valid.
# Only valid emails are returned by the function.
# A valid email address will have the following: 
# the @ symbol (if the @ symbol is at the beginning of the name, the email is invalid).
# If there is more than one @ sign, the email is invalid.
# All valid emails must end with a dot com (.com); otherwise, the email is invalid.

emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']

# For example, the list of emails above should output the following emails as valid emails:
# ['ben@mail.com', 'kenny@gmail.com]
# If no emails in the list are valid, the function should return 'All emails are invalid.'
