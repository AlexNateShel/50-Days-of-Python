# Write a function called 'your_vat'.
# The function has no parameters.
# The function asks the user to input the price of an item and VAT (VAT should be a percentage).
# The function should return the price of the item plus VAT.
# If the price is 220 and the VAT is 15%, your code should return a VAT-inclusive price of 253.
# Check to see if your code can handle ValueError and negative inputs from the user.
# Ensure the code runs until valid numers are entered.
# (Hint: Your code should include a while loop).

def your_vat():
    while True:
        try:
            price = int(input('Enter the price: '))
            vat = int(input('Enter the VAT: '))

            if price > 0 and vat > 0:
                total_price = price + \
                            (price * vat / 100 + 1) - 1
                return 'The price VAT inclusive is', total_price
            else:
                print('Please enter non-negative values.')
        except ValueError:
            print('Please enter a valid number.')

print(your_vat())