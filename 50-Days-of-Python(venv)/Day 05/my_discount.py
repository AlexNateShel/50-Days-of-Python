# Create a function called 'my_discount'.
# The function takes no arguments but asks the user to input the price and discount (percentage) of the product.
# Once the user inputs the price and the discount, it calculates the price after discount. 
# The function should return the price after the discount.
# For example, if the user enters '150' as the price and '15%' as the discount, your function should return '127.5'.

def my_discount():
    price = input('Enter the price: ')
    discount = input('Enter the discount: ')
    price = float(price)
    discount = float(discount) * 0.01
    discount_rate = price * discount
    adjusted_price = price - discount_rate
    return adjusted_price

print(my_discount())
