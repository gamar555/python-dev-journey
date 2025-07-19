# Simulates conditional logic during checkout process

# cart_total = float(input("Enter your cart total: $"))  # Get the total amount from the user

# has_coupon = input("Do you have a disscount coupon? (yes/no): ").strip().lower()  # Check if the user has a coupon  

# if cart_total >= 500:  # If the user has a coupon
#     print("You're elegible for a free delivery!")   # Notify the user about the discount

#     if has_coupon == "yes":
#         print("Extra discount applied!")  # Apply extra discount if the user has a coupon
#     else:
#         print("You could save more with a coupon!")  # Encourage the user to use a coupon
# else:
#     print("Delivery charges apply.")  # Notify the user about delivery charges
#     print(f"Your final amount is: ${cart_total:.2f}")  # Display the final amount to the user
# # This code simulates a simple checkout process for an online shopping cart.


# I want to zomato checkout process with conditional logic

def checkout(cart_total, has_coupon):
    """ We want to simulate a checkout process with conditional logic"""
    
    if cart_total >= 1000:
        print("You're elegible for free delivery!") # Notify the user about free delivery

        if has_coupon.lower() == "yes":
            print("Extra discount applied!") # Apply extra discount if the user has a coupon
        else:
            print("You could save more items for free delivery!") # Encourage the user to use a coupon
    else:
        print("Delivery charges apply.") # Notify the user about delivery charges
        print(f"Your final amount is: ${cart_total:.2f}") # Display the final amount to the user

cart_total = float(input("Enter your cart total: $"))    # Get the total amount from the user
has_coupon = input("Do you have a discount coupon? (yes/no): ").strip().lower()  # Check if the user has a coupon
checkout(cart_total, has_coupon)  # Call the checkout function with the provided cart total and coupon status
# This code simulates a checkout process for an online shopping cart with conditional logic.
# It checks if the cart total is above a certain threshold for free delivery and applies discounts based
# on whether the user has a coupon. The final amount is displayed to the user.
# The code uses a function to encapsulate the checkout logic, making it reusable and organized.




