password = "1234"
count = 0
correct = False


while count < 3:
    guess = input("enter the password")
    count = count + 1

    if guess == password:
        print("Authentication Success")
        correct = True
        break
    else:
        if count < 3:
            print("Try again")
        

if not correct:
    print("Authentication Failed")