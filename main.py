alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

msg = input("\nEnter a message: ").lower()

shift_input = input("\nEnter a shift number: ")

shift_input_int = int(shift_input)

def encrypt(plain_text, shift):

    encrypted_word = ""

    for letter in plain_text:

        place = alphabet.index(letter)

        new_place = place + shift
        
        new_letter = alphabet[new_place]

        encrypted_word += new_letter

    print(f"\nThe encrypted version is {encrypted_word}")


def decode(plain_text, shift):

    decrypted_word = ""

    for letter in plain_text:
        place = alphabet.index(letter)

        new_place = place - shift

        new_letter = alphabet[new_place]

        decrypted_word += new_letter
    print(f"\nThe decrypted version is {decrypted_word}")

if direction == "encode":
    encrypt(plain_text=msg , shift= shift_input_int)
elif direction == "decode":
    decode(plain_text=msg, shift=shift_input_int)
else:
    print("Error you did not enter a valid input")

input("\nPress any key to exit")

