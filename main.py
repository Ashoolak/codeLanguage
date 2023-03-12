alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def code(message, change, function):
    final = ""
    if function == "decode":
        change *= -1
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            extra = index + change
            if extra < 0:
                final += alphabet[extra + 26]
            elif extra > 25:
                final += alphabet[extra - 26]
            else:
                final += alphabet[extra]
        else:
            final += letter
    return final


repeat = True

while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift >= 26:
        shift -= 26
    print(code(text, shift, direction))
    again = input("Do you want to go again? Enter y or n")
    if again == "n":
        repeat = False

