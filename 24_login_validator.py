"""
Problem 24: Login Validator
Statement: Login Validator: Check whether a username and password combination is valid
"""

# Predefined valid credentials for demonstration
valid_username = "admin"
valid_password = "admin123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == valid_username and password == valid_password:
    print("Login Successful")
else:
    print("Login Failed: Invalid username or password")
