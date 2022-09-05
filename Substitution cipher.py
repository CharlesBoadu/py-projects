def sub_cipher(plaintext):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    sub = 'zyxwvutsrqponmlkjihgfedcba'
    
    cipher = ''

    for plain_char in plaintext:
        if plain_char == ' ':
            cipher += ' '
        else:
            for alp_char in alp:
                if plain_char.lower() == alp_char:
                    char_index = alp.index(alp_char)
                    cipher += sub[char_index]

    return cipher

plaintext = 'Hello World'
print(plaintext)
print(sub_cipher(plaintext), ' -----> Substitution cipher')
