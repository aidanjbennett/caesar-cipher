from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift, direction):

    word = ""

    if direction == "decode":
        shift *= -1

    for char in plain_text:

        if char in alphabet:

            place = alphabet.index(char)

            new_place = place + shift

            new_letter = alphabet[new_place]

            word += new_letter
        else:
            word += char

    print(f"\nThe {direction} version is {word}")


should_contine = True

while should_contine:

    direction_input = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text_input = input("\nEnter a message: ").lower()

    shift_input = input("\nEnter a shift number: ")

    shift_input_int = int(shift_input)

    shift_input_int = shift_input_int % 26

    caesar(plain_text=text_input, shift=shift_input_int,
           direction=direction_input)

    user_continue = input("Do you want to continue enter 'Y' to contine or 'N' to exit").lower()

    if user_continue == "y":
        should_contine = True
    elif user_continue == "n":
        should_contine == False
        print("Goodbye hope you enjoyed using the program")
    else:
        print("No valid input exiting program")
        should_contine = False