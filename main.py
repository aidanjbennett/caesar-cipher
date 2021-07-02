alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text_input = input("\nEnter a message: ").lower()

shift_input = input("\nEnter a shift number: ")

shift_input_int = int(shift_input)

def caesar(plain_text, shift, direction):
    
    word = ""

    for letter in plain_text:

        place = alphabet.index(letter)

        if direction == "decode":
           shift *= -1
        
        new_place = place + shift
        
        new_letter = alphabet[new_place]

        word += new_letter

    print(f"\nThe {direction} version is {word}")

caesar(plain_text=text_input, shift=shift_input_int, direction=direction_input)

input("\nPress any key to exit")

