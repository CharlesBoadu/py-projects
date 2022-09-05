def shift_cipher(key, plain_text):
    plain_text = plain_text.lower()
    alp = 'abcdefghijklmnopqrstuvwxyz'
    key_num = alp.index(key.lower())
    cipher = ''
    for char in plain_text:
        if char == ' ':
            cipher += ' '
        else:
            for alp_char in alp:
                if alp_char == char:
                    rem = alp.index(alp_char) + key_num % 26
                    if rem > 25:
                        cipher += alp[rem - 26]
                    else:
                        cipher += alp[rem]
                    

    return cipher

key = 'u'
plain_text = 'Decryption Methods'
shift_cipher = shift_cipher(key, plain_text)

print(plain_text)
for i in range(len(plain_text)):
    if plain_text[i] == ' ':
        print(' ', end='')
    else:
        print(key, end='')
print('\n')

for j in range(len(plain_text)):    
    print('_', end='')    
print('\n')
print(shift_cipher, end='  -----> Shift Cipher \n')

for k in range(len(plain_text)):
    print('_', end='')
    
