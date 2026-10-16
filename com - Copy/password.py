import getpass

user_password = getpass.getpass("Enter your password: ")

if user_password == "secret123":
    print("Access granted :)")
else:
    print("Access denied!")