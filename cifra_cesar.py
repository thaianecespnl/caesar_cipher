alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(star_text, shift_amount, cipher_direction):
        n = len(alphabet)
        end_text = ""
        if cipher_direction == "decode":
                shift_amount *= -1
        for char in star_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[(new_position)%n]
            else:
                end_text += char
        print (f"Here's the {cipher_direction} result: {end_text}")

    caesar (star_text= text, shift_amount=shift, cipher_direction=direction)

    result = (input("Do you want to restart?\n yes or no:\n")).lower()
    if result == "no":
        restart = False
        print ("Thank you for using our cipher. Have a nice day!")