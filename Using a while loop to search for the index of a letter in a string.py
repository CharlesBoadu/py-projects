string = input("Enter a string: ")
letter = input("Enter a letter: ")

i = 0
while i < len(string):
    a = string[i]
    if a == letter:
        print("The index of the letter is", i)
        break
    elif letter not in string:
        print("String does not contain letter")
        break
    else:
        i += 1



#Searching for the index of a character in a string using a for loop
string = input("Enter a string: ")
letter = input("Enter a letter: ")

for i in range(len(string)):
    if string[i] == letter:
        print("The index of the letter is", i)
        break
    elif letter not in string:
        print("String does not contain letter")
        break
