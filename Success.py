class Password_manager:

    def __init__(self, old_passwords):
        self.old_passwords = ['1234', '5678', '4321']

    def get_password(self):
        for i in range(len(self.old_passwords)):
            current_password = self.old_passwords[i]

        return current_password

    def set_password(self):
        attempted_password = input("Enter the password: ")
        for i in range(len(self.old_passwords)):
            current_password = self.old_passwords[i]

        if attempted_password not in self.old_passwords:
            attempted_pasword = current_password
            print(attempted_password)
                

    def is_correct(self, string):
        if string in self.old_passwords:
            return True
        else:
            return False
            
e = Password_manager('1234')
e.set_password()
print("Is the string the same as the current password?\nAnswer:", e.is_correct('4322'))
print("The current password is", e.get_password())


