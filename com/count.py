import getpass

count = 0

while True:
    user_password = getpass.getpass("Enter your password: ")

    if user_password == "secret123":
        print("Access granted :)")
        print(f"count = {count}")
        break
    else:
        print("Access denied!")
        count += 1