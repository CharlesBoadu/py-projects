def matches(string1, string2):
    match = 0
    for char1 in string1:
        for char2 in string2:
            if char1 == char2:
                match += 1

    print(match, 'matches exist')

matches('pyhton', 'path')
