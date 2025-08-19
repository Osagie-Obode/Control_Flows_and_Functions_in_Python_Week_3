# Week 3 Assignment: Discount Calculator

def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price based on the original price and discount percentage.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount rate as a percentage (0-100).

    Returns:
    float: The final price after applying the discount.
    """
    if discount_percent > 20:
        discount_amount = (discount_percent / 100) * price
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price
    
# Example usage:
Price = float(input("Enter the original price: "))
Discount_Percent = float(input("Enter the discount percentage: "))
print(f"The price after discount is: {calculate_discount(Price, Discount_Percent)}")