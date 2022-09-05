def caesar_cipher(plaintext):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    
    for char in plaintext:
        if char == ' ':
            cipher += ' '
        else:
            for alp_char in alp:
                if char.lower() == alp_char:
                    shift = alp.index(alp_char) + 3
                    cipher += alp[shift]
    return cipher

plaintext = 'apple'
print(plaintext)
print(caesar_cipher(plaintext), ' -----> Caesar cipher')
