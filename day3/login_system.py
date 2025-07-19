# Simple login logic for internal tool

def login(username, password): # function named 'login'takes two inputs
    """
    Verifies login credentaials for an internal system."""
    if username == 'admin' and password == "secure123": # check both conditions
        print("Login successful! Access granted to {username}.") # if both match show, success message
    else:
        print("Invaild username or password try again.") # if not match show error message

# Example usage of the login function
username = input("Username ") # Ask the user to type a username and save it in variable 'username'
password = input("Password ") # Ask the user to type a password and save it in variable 'password'
login(username, password) # Call the login function with the provided username and password

