def check_password(password):
    count = 0

    while count < 3:
        guess = input("Enter the password: ")
        count += 1

        if guess == password:
            return True
        else:
            if count < 3:
                print("Try again")

    return False

password = input("Make password: ")
is_correct = check_password(password)

if is_correct:
    print("Authentication Successful")
else:
    print("Authentication Failed")