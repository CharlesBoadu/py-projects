def findall(string, character):
    pos_list = []
    string_list = list(string)
    for i in range(len(string_list)):
        if string_list[i] == character:
            pos_list.append(i)

    print("Locations of the character", "'"+character+"'", "is at indexes", pos_list)

findall('character', 'a')
