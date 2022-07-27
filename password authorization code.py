correct_password = "devastation"
number_of_tries = 5
tries = 0
while tries < number_of_tries:
    password = input("Enter your password: ")
    if password != correct_password and tries <= 3:
        print("Password Incorrect! please try again!")
        tries += 1
    elif password != correct_password and tries == 4:
        print("Password incorrect! You have been kicked out of the system!")
        break
    else:
        print("You are logged on into the system")
        break
