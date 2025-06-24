# We are creating a Caesar Cipher program that can encrypt and decrypt messages.

# TODO 7 - If there is a space in the message, we should keep it as is.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def CaesarCipher():
    # TODO 1 - We greet the user and ask them if they want to encrypt or decrypt a message.
    print("Welcome to the Caesar Cipher program!")
    mode = input("Do you want to encrypt or decrypt the message? (e/d): ").lower()

    if mode not in ['e', 'd']:
        print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")
        return

    # TODO 2 - We ask the user for the message they want to encrypt or decrypt.
    message = input("Please enter the message: ").lower()

    # TODO 3 - We ask the user for the shift value.
    shift = int(input("Please enter the shift value (1-25): "))

    if shift < 1 or shift > 25:
        print("Invalid shift value. Please enter a number between 1 and 25.")
        return

    # TODO 4 - If the user wants to encrypt, we call the encrypt function. We are using indexing to find the position of each character in the alphabet and shifting it accordingly.

    if mode == 'e':
        encrypted_message = ''
        for char in message:
            # TODO 7 - If there is a space in the message, we should keep it as is.
            if char == ' ':
                encrypted_message += ' '
            
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index + shift) % 26
                encrypted_message += alphabet[new_index]

    # TODO 5 - If the user wants to decrypt, we call the decrypt function. We are using indexing to find the position of each character in the alphabet and shifting it accordingly.
    else:
        decrypted_message = ''
        for char in message:
            # TODO 7 - If there is a space in the message, we should keep it as is.
            if char == ' ':
                decrypted_message += ' '
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index - shift) % 26
                decrypted_message += alphabet[new_index]


    # TODO 6 - We print the result of the encryption or decryption.
    if mode == 'e':
        print("Encrypted message:", encrypted_message)
    else:
        print("Decrypted message:", decrypted_message)


CaesarCipher()




