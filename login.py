print("Login to system")

# Get username and password from user
username = input("Enter username: ")
password = input("Enter password: ")

# Check if username and password are correct
if username == "admin" and password == "1234":
    print("Login success")
else:
    print("Login fail")
