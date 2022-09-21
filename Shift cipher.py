#function that accepts plaintext and key to encrypt the plaintext using the key
def shift_cipher_encrypt(key, plain_text):
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

#Function that accepts the ciphertext and key and decrypts the ciphertext using the key
def shift_cipher_decrypt(key, cipher_text):
    cipher_text = cipher_text.lower()
    alp = 'abcdefghijklmnopqrstuvwxyz'
    key_num = alp.index(key.lower())
    decrypt = ''
    for char in cipher_text:
        if char == ' ':
            decrypt += ' '
        else:
             for alp_char in alp:
                if alp_char == char:
                    rem = alp.index(alp_char) - key_num % 26
                    if rem < 0:
                        decrypt += alp[26 + rem]
                    else:
                        decrypt += alp[rem]
    return decrypt

#Function to print plaintext, key and show the corresponding ciphertext
def encryption(key):
    print('ENCRYPTION WITH THE KEY, "', key, '" USING SHIFT CIPHER \n')
    print(plain_text.upper(), '------> Plaintext')
    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            print(' ', end='')
        else:
            print(key, end='')
    print('\n')

    for j in range(len(plain_text)):    
        print('_', end='')    
    print('\n')
    print(shift_cipher_encryption.upper(), end='  -----> Encrypted Plaintext \n')

    for k in range(len(plain_text)):
        print('_', end='')

#Function to print ciphertext, key and show the corresponding plaintext
def decryption(key):
    print('DECRYPTION WITH THE KEY, "', key,'" USING SHIFT CIPHER\n')
    print(cipher_text.upper(), '-----> Ciphertext')
    for i in range(len(cipher_text)):
        if cipher_text[i] == ' ':
            print(' ', end='')
        else:
            print(key, end='')
    print('\n')

    for j in range(len(cipher_text)):    
        print('_', end='')    
    print('\n')
    print(shift_cipher_decryption.upper(), end='  -----> Decrypted Ciphertext \n')

    for k in range(len(plain_text)):
        print('_', end='')

#Function to decide if user wants to either encrypt or decrypt again
def decision():
        user_dec = ''
        while user_dec != 'yes' or user_dec != 'no':
            user_dec = input("Use Program again? Type 'yes' to continue and 'no' to end program: ")
            if user_dec == 'yes':
                end_prog = False
                return end_prog
            elif user_dec == 'no':
                end_prog = True
                return end_prog
            else:
                print("invalid input")

end_prog = False
while end_prog == False:
    op = input("Hello, type 'enc' to 'Encrypt' or 'dec' to 'Decrypt': ") 
    if op == 'enc':
        plain_text = input("What is the plaintext to be encrypted: ")
        key = input("What is the key: ")
        shift_cipher_encryption = shift_cipher_encrypt(key, plain_text)
        encryption(key)
        print('\n')
        end_prog = decision()
    elif op == 'dec':
        cipher_text = input("What is the ciphertext to be decrypted: ")
        key = input("What is the key: ")
        shift_cipher_decryption = shift_cipher_decrypt(key, cipher_text)
        decryption(key)
        print('\n')
        end_prog = decision()
    else:
        print("Invalid input")

print("Thanks for using Shift Cipher program! Bye!")








    
