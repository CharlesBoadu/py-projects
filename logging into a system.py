account_dictionary = {}
for i in range(5):
    user_name = input("Enter your user name: ")
    password = int(input("Enter your password: "))
    account_dictionary[user_name] = password

print('\n',account_dictionary,'\n')
user_name = ""

for i in range(10):
    user_name = input("Enter your username: ")
    if user_name not in account_dictionary:
        print("Not a valid user of the system.")
    else:
        login_password = int(input("Enter your password: "))
        if login_password == account_dictionary[user_name]:
            print("You are logged into the system!")
            break
        else:
            print("Password Invalid!")
            


