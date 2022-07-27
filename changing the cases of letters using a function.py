def change_case(string):
    for word in string:
        if word == word.upper():
            string = string.replace(word.upper(), word.lower())
        else:
            string = string.replace(word.lower(), word.upper())

    print(string)

change_case('ChArLeS')
